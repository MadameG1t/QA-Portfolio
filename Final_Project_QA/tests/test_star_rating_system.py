import pytest

from pages.star_rating_system_gate_page import StarRatingSystemGate


@pytest.fixture
def star_page(driver, purchased_product):
    return StarRatingSystemGate(driver)


def test_user_can_delete_written_feedback(star_page, driver):

    page = star_page

    page.delete_my_review()

    page.select_star(5)
    page.enter_review_text("Posting again after delete (automation).")
    page.click_send()

    restriction = page.get_restriction_message_safe().lower()
    assert "already reviewed" not in restriction, f"Still blocked after delete: {restriction}"


def test_zero_star_rating_is_invalid(star_page):

    page = star_page

    page.enter_review_text("Submitting without selecting stars.")
    page.click_send()

    msg = (page.get_error_text() or page.get_restriction_message_safe()).strip()
    assert "data entry invalid" in msg.lower(), f"Expected invalid-entry message, got: {msg}"


def test_rating_submission_updates_review_count_integration(star_page, driver):

    page = star_page

    before = page.get_display_review_count()

    page.select_star(4)
    page.enter_review_text("Integration test: 4-star rating.")
    page.click_send()

    driver.refresh()

    after = page.get_display_review_count()
    assert after == before + 1, f"Review count did not increment: before={before}, after={after}"
