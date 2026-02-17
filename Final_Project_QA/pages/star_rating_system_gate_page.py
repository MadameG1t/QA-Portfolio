import re
import time

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoAlertPresentException
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
    REVIEW_TEXTAREA = (By.CSS_SELECTOR, "textarea.new-review-form-control[placeholder='What is your view?']")
    SEND_BTN = (By.CSS_SELECTOR, "button.new-review-btn-send")

    REVIEW_RESTRICTION_TEXT = (By.CSS_SELECTOR, "div.reviewRestriction p")
    ERROR_TEXT = (
        By.CSS_SELECTOR,
        "[role='alert'], [role='status'], .error, .alert, .text-danger, .invalid-feedback"
    )

    DISPLAY_RATING_CONTAINER = (By.CSS_SELECTOR, ".ratingContainer .custom-rating")
    DISPLAY_REVIEW_COUNT = (By.CSS_SELECTOR, ".ratingContainer .reviews")

    MENU_ICON = (By.CSS_SELECTOR, "div.menu-icon")
    DELETE_BTN = (By.XPATH, "//button[normalize-space()='Delete' or normalize-space()='Remove']")

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

    def wait_for_form_or_restriction(self, timeout: int = 10) -> None:
        def _predicate(d):
            try:
                textarea = d.find_element(*self.REVIEW_TEXTAREA)
                stars = d.find_element(*self.INTERACTIVE_RATING)
                if textarea.is_displayed() and stars.is_displayed():
                    return True
            except Exception:
                pass

            try:
                r = d.find_element(*self.REVIEW_RESTRICTION_TEXT)
                if r.is_displayed() and (r.text or "").strip() != "":
                    return True
            except Exception:
                pass

            return False

        WebDriverWait(self.driver, timeout).until(_predicate)

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
        self.wait_for_form_or_restriction(timeout=8)

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

    def get_display_review_count_text(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.DISPLAY_REVIEW_COUNT)).text.strip()

    def get_display_review_count(self) -> int:
        text = self.get_display_review_count_text()
        m = re.search(r"\((\d+)\)", text)
        return int(m.group(1)) if m else 0

    def open_review_menu(self) -> None:
        try:
            restriction = self.driver.find_element(*self.REVIEW_RESTRICTION_TEXT)
            if restriction.is_displayed() and restriction.text.strip() != "":
                menu_near_restriction = self.driver.find_element(
                    By.XPATH,
                    "//div[contains(@class,'reviewRestriction')]"
                    "/preceding::div[contains(@class,'menu-icon')][1]"
                )
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", menu_near_restriction)
                try:
                    menu_near_restriction.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", menu_near_restriction)
                return
        except Exception:
            pass

        menus = self.wait.until(EC.presence_of_all_elements_located(self.MENU_ICON))
        for m in menus:
            if m.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", m)
                try:
                    m.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", m)
                return
        raise AssertionError("No visible review menu icon found.")

    def wait_until_review_posted(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: (
                    len(d.find_elements(*self.MENU_ICON)) > 0
                    or "already reviewed" in d.page_source.lower()
            )
        )

    def click_delete(self) -> None:
        buttons = self.driver.find_elements(*self.DELETE_BTN)
        for b in buttons:
            if b.is_displayed() and b.is_enabled():
                try:
                    b.click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", b)
                return
        raise AssertionError("No visible Delete button found after opening the review menu.")

    def confirm_browser_delete_popup(self, timeout: int = 6) -> None:
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()

    def delete_my_review(self, product_url: str = Urls.PRODUCT_ORANGES, attempts: int = 4) -> None:
        self.driver.get(product_url)
        self.driver.refresh()

        for i in range(attempts):

            if self.is_review_form_visible():
                return

            try:
                self.open_review_menu()
                time.sleep(0.5)
                self.click_delete()
            except Exception:

                self.driver.refresh()
                time.sleep(1)
                continue

            try:
                alert = WebDriverWait(self.driver, 6).until(EC.alert_is_present())
                alert.accept()
            except TimeoutException:

                pass
            except NoAlertPresentException:
                pass

            time.sleep(1)
            self.driver.get(product_url)
            self.driver.refresh()

            try:
                self.wait_for_form_or_restriction(timeout=10)
            except TimeoutException:
                pass


            if self.is_review_form_visible():
                return

            restriction = self.get_restriction_message_safe().lower()
            if "already reviewed" not in restriction:
                return

        restriction = self.get_restriction_message_safe()
        raise AssertionError(
            f"Delete did not take effect after {attempts} attempts. Restriction: '{restriction}'"
        )


    def is_review_form_visible(self) -> bool:
        try:
            header = self.driver.find_elements(*self.ADD_COMMENT_HEADER)
            stars = self.driver.find_elements(*self.INTERACTIVE_RATING)
            textarea = self.driver.find_elements(*self.REVIEW_TEXTAREA)

            return (
                    len(header) > 0 and header[0].is_displayed()
                    and len(stars) > 0 and stars[0].is_displayed()
                    and len(textarea) > 0 and textarea[0].is_displayed()
            )
        except Exception:
            return False
