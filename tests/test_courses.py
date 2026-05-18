from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    cours_elements = [
        page.get_by_test_id("courses-list-toolbar-title-text"),
        page.get_by_test_id("courses-list-empty-view-icon"),
        page.get_by_test_id("courses-list-empty-view-title-text"),
        page.get_by_test_id("courses-list-empty-view-description-text"),
    ]
        
    for element in cours_elements:
        expect(element).to_be_visible()

    expect(cours_elements[0]).to_have_text("Courses")
    expect(cours_elements[2]).to_have_text("There is no results")
    expect(cours_elements[3]).to_have_text("Results from the load test pipeline will be displayed here")
