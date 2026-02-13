import pytest

from pages.star_rating_system_gate_page import StarRatingSystemGate
from utils.constants import Urls


@pytest.fixture
def star_page(driver, purchased_product):
    return StarRatingSystemGate(driver)

def test_user_cannot_review_without_purchase(driver):
    driver.get(Urls.PRODUCT_ORANGES)
    page = StarRatingSystemGate(driver)

    message = page.get_restriction_message_safe()
    assert "You need to buy this product" in message

def test_user_can_delete_written_feedback(star_page, driver):
    page = star_page

    before = page.get_display_review_count()

    page.add_review(stars=5, text="Test review to delete")
    mid = page.get_display_review_count()
    assert mid >= before + 1, "Review count did not increase after adding a review."

    page.delete_my_review()
    after = page.get_display_review_count()
    assert after <= mid - 1, "Review count did not decrease after deleting the review."

def test_zero_star_rating_is_invalid(star_page, driver):
    page = star_page

    before = page.get_display_review_count()

    page.enter_review_text("Submitting without selecting stars.")
    page.click_send()
    assert "Data entry invalid" in page.get_error_text()

    driver.refresh()
    after = page.get_display_review_count()

    assert after == before, "Review count should not change when no star is selected."

def test_rating_submission_updates_review_count_integration(star_page, driver):

    page = star_page

    before = page.get_display_review_count()

    page.select_star(4)
    page.enter_review_text("Integration test: 4-star rating.")
    page.click_send()

    driver.refresh()

    after = page.get_display_review_count()
    assert after == before + 1, f"Review count did not increment: before={before}, after={after}"
