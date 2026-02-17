import re

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.constants import Urls


class StarRatingSystemGate:

    ADD_COMMENT_HEADER = (By.XPATH, "//h5[normalize-space()='Add a comment']")
    INTERACTIVE_RATING = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating")

    STAR_1 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(1)")
    STAR_2 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(2)")
    STAR_3 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(3)")
    STAR_4 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(4)")
    STAR_5 = (By.CSS_SELECTOR, ".new-review-rating-stars .interactive-rating span.star:nth-child(5)")

    REVIEW_FORM_CONTAINER = (By.CSS_SELECTOR, "div.new-review-card-body")
    REVIEW_FORM_HEADING = (
    By.XPATH, "//div[contains(@class,'new-review-card-body')]//h5[normalize-space()='Add a comment']")
    REVIEW_TEXTAREA = (By.CSS_SELECTOR, "textarea.new-review-form-control[placeholder='What is your view?']")
    SEND_BTN = (By.CSS_SELECTOR, "button.new-review-btn-send")

    REVIEW_RESTRICTION_TEXT = (By.CSS_SELECTOR, "div.reviewRestriction p")
    ERROR_TEXT = (
        By.CSS_SELECTOR,
        "[role='alert'], [role='status'], .error, .alert, .text-danger, .invalid-feedback"
    )

    DISPLAY_RATING_CONTAINER = (By.CSS_SELECTOR, ".ratingContainer .custom-rating")
    DISPLAY_REVIEW_COUNT = (By.CSS_SELECTOR, ".ratingContainer .reviews")

    MENU_ICON = (By.CSS_SELECTOR, "div.menu-icon")  # if site changes, update this
    DELETE_BTN = (By.XPATH, "//button[normalize-space()='Delete' or normalize-space()='Remove']")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[normalize-space()='Confirm' or normalize-space()='Yes' or normalize-space()='Delete']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _click_locator(self, locator) -> None:

        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", el)

    def _scroll_to_review_section(self) -> None:

        try:
            header = self.wait.until(EC.visibility_of_element_located(self.ADD_COMMENT_HEADER))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        except TimeoutException:

            self.driver.execute_script("window.scrollBy(0, 700);")

    def select_star(self, stars: int) -> None:
        if stars not in (1, 2, 3, 4, 5):
            raise ValueError("stars must be an integer between 1 and 5")

        locator_map = {1: self.STAR_1, 2: self.STAR_2, 3: self.STAR_3, 4: self.STAR_4, 5: self.STAR_5}

        self._scroll_to_review_section()
        self.wait.until(EC.visibility_of_element_located(self.INTERACTIVE_RATING))
        self._click_locator(locator_map[stars])

    def enter_review_text(self, text: str) -> None:
        self._scroll_to_review_section()

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
        self._scroll_to_review_section()
        self._click_locator(self.SEND_BTN)

    def add_review(self, stars: int, text: str) -> None:

        self.select_star(stars)
        self.enter_review_text(text)
        self.click_send()

        WebDriverWait(self.driver, 5).until(lambda d: True)

    def get_restriction_message_safe(self) -> str:
        try:
            return self.wait.until(EC.visibility_of_element_located(self.REVIEW_RESTRICTION_TEXT)).text.strip()
        except TimeoutException:
            return ""

    def get_error_text(self) -> str:
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT))
            return el.text.strip()
        except TimeoutException:
            return ""

    def get_display_review_count_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.DISPLAY_REVIEW_COUNT)).text.strip()

    def get_display_review_count(self) -> int:
        text = self.get_display_review_count_text()
        m = re.search(r"\((\d+)\)", text)
        return int(m.group(1)) if m else 0

    def open_review_menu(self) -> None:
        self._scroll_to_review_section()

        try:
            menus = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.MENU_ICON))
        except TimeoutException:
            raise AssertionError("No review menu icon found (likely no review exists yet for this user).")

        for m in menus:
            if m.is_displayed():
                try:
                    m.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", m)
                return

        raise AssertionError("Review menu icons exist, but none are visible/clickable.")

    def is_review_form_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_COMMENT_HEADER))
            self.wait.until(EC.visibility_of_element_located(self.INTERACTIVE_RATING))
            self.wait.until(EC.visibility_of_element_located(self.REVIEW_TEXTAREA))
            return True
        except TimeoutException:
            return False

    def refresh_product_page(self, product_url: str) -> None:

        self.driver.get(product_url)

        def _form_or_restriction_visible(d):
            try:
                form = d.find_element(*self.REVIEW_TEXTAREA)
                if form.is_displayed():
                    return True
            except Exception:
                pass
            try:
                r = d.find_element(*self.REVIEW_RESTRICTION_TEXT)
                if r.is_displayed() and r.text.strip() != "":
                    return True
            except Exception:
                pass
            return False

        WebDriverWait(self.driver, 10).until(_form_or_restriction_visible)

    def delete_my_review(self, product_url: str = Urls.PRODUCT_ORANGES) -> None:
        self.open_review_menu()
        self.click_delete()
        self.confirm_browser_delete_popup(timeout=5)

        self.driver.get(product_url)

        if not self.is_review_form_visible():
            restriction = self.get_restriction_message_safe()
            raise AssertionError(
                "Delete may have failed: review form did not re-appear. "
                f"Restriction message (if any): '{restriction}'"
            )
    def click_delete(self) -> None:
        self._click_locator(self.DELETE_BTN)

    def confirm_browser_delete_popup(self, timeout=5):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()
