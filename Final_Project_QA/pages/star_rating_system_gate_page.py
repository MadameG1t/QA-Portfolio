import re

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls


class StarRatingSystemGate:

    INTERACTIVE_RATING = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating")

    STAR_1 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(1)")
    STAR_2 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(2)")
    STAR_3 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(3)")
    STAR_4 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(4)")
    STAR_5 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(5)")

    REVIEW_TEXTAREA = (By.CSS_SELECTOR, "textarea.new-review-form-control")
    SEND_BTN = (By.CSS_SELECTOR, "button.new-review-btn-send")


    REVIEW_RESTRICTION_TEXT = (By.CSS_SELECTOR, "div.reviewRestriction p")
    ERROR_TEXT = (By.CSS_SELECTOR, "[role='alert'], .error, .alert, .text-danger, .invalid-feedback")


    DISPLAY_RATING_CONTAINER = (By.CSS_SELECTOR, ".ratingContainer .custom-rating")
    DISPLAY_REVIEW_COUNT = (By.CSS_SELECTOR, ".ratingContainer .reviews")


    MENU_ICON = (By.CSS_SELECTOR, "div.menu-icon")
    EDIT_BTN = (By.XPATH, "//button[normalize-space()='Edit']")
    DELETE_BTN = (By.XPATH, "//button[normalize-space()='Delete' or normalize-space()='Remove']")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[normalize-space()='Confirm' or normalize-space()='Yes' or normalize-space()='Delete']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)



    def select_star(self, stars: int) -> None:
        if stars not in (1, 2, 3, 4, 5):
            raise ValueError("stars must be an integer between 1 and 5")

        locator_map = {
            1: self.STAR_1,
            2: self.STAR_2,
            3: self.STAR_3,
            4: self.STAR_4,
            5: self.STAR_5,
        }

        self.wait.until(EC.visibility_of_element_located(self.INTERACTIVE_RATING))
        self._click_with_retry(locator_map[stars])

    def enter_review_text(self, text: str) -> None:
        last_exc = None
        for _ in range(2):
            try:
                field = self.wait.until(EC.visibility_of_element_located(self.REVIEW_TEXTAREA))
                field.clear()
                field.send_keys(text)
                return
            except StaleElementReferenceException as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def click_send(self) -> None:
        try:
            self._click_with_retry(self.SEND_BTN)
        except TimeoutException:
            # Fallback for cases where the button is visible but not "clickable"
            btn = self.wait.until(EC.visibility_of_element_located(self.SEND_BTN))
            self.driver.execute_script("arguments[0].click();", btn)

    def _click_with_retry(self, locator, attempts: int = 2) -> None:
        last_exc = None
        for _ in range(attempts):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except StaleElementReferenceException as exc:
                last_exc = exc
        if last_exc:
            raise last_exc

    def is_send_enabled(self) -> bool:
        last_exc = None
        for _ in range(2):
            try:
                btn = self.wait.until(EC.visibility_of_element_located(self.SEND_BTN))
                disabled_attr = (btn.get_attribute("disabled") or "").strip().lower()
                class_attr = (btn.get_attribute("class") or "").lower()
                return btn.is_enabled() and disabled_attr == "" and "disabled" not in class_attr
            except StaleElementReferenceException as exc:
                last_exc = exc
        if last_exc:
            raise last_exc
        return False

    def get_restriction_message(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.REVIEW_RESTRICTION_TEXT)).text.strip()

    def get_restriction_message_safe(self) -> str:
        try:
            return self.wait.until(EC.visibility_of_element_located(self.REVIEW_RESTRICTION_TEXT)).text.strip()
        except TimeoutException:
            return ""

    def get_error_text(self) -> str:
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT)).text.strip()
        except TimeoutException:
            return ""


    def interactive_stars(self):
        self.wait.until(EC.visibility_of_element_located(self.INTERACTIVE_RATING))
        container = self.driver.find_element(*self.INTERACTIVE_RATING)
        return container.find_elements(By.CSS_SELECTOR, "span.star")

    def count_non_empty_interactive_stars(self) -> int:
        stars = self.interactive_stars()
        count = 0
        for s in stars:
            cls = (s.get_attribute("class") or "").lower()
            if "empty" not in cls:
                count += 1
        return count

    def display_rating_exists(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.DISPLAY_RATING_CONTAINER))
            return True
        except Exception:
            return False

    def get_display_review_count_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.DISPLAY_REVIEW_COUNT)).text.strip()

    def get_display_review_count(self) -> int:

        text = self.get_display_review_count_text()
        m = re.search(r"\((\d+)\)", text)
        return int(m.group(1)) if m else 0

    def open_review_menu(self) -> None:
        menus = self.wait.until(EC.presence_of_all_elements_located(self.MENU_ICON))
        for m in menus:
            if m.is_displayed():
                m.click()
                return
        raise AssertionError("No visible review menu icon found for this user.")

    def click_edit(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.EDIT_BTN)).click()

    def click_delete(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.DELETE_BTN)).click()

    def confirm_delete_if_present(self) -> None:

        try:
            alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            alert.accept()
            return
        except TimeoutException:
            pass

        try:
            self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN)).click()
        except TimeoutException:
            pass

    def delete_my_review(self) -> None:
        self.open_review_menu()
        self.click_delete()
        self.confirm_delete_if_present()

        try:
            self.wait.until(EC.invisibility_of_element_located(self.MENU_ICON))
        except TimeoutException:
            pass

        # Reload via shop to ensure the review state updates server-side.
        self.driver.get(Urls.STORE)
        self.driver.get(Urls.PRODUCT_ORANGES)
        try:
            self.wait.until(EC.visibility_of_element_located(self.REVIEW_TEXTAREA))
        except TimeoutException:
            pass
