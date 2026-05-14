from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        
        page.get_by_test_id("registration-form-email-input").locator("input").fill("user.name@gmail.com")
        page.get_by_test_id("registration-form-username-input").locator("input").fill("username")
        page.get_by_test_id("registration-form-password-input").locator("input").fill("password")
        page.get_by_test_id("registration-page-registration-button").click()
        
        context.storage_state(path="browser-state.json")
        browser.close()
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        
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
        
        browser.close()