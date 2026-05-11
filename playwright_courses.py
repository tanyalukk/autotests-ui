from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    email_input = (
        page.get_by_test_id("registration-form-email-input")
        .locator("input")
        .fill("user.name@gmail.com")
    )

    username_input = (
        page.get_by_test_id("registration-form-username-input")
        .locator("input")
        .fill("username")
    )

    password_input = (
        page.get_by_test_id("registration-form-password-input")
        .locator("input")
        .fill("password")
    )

    registration_button = page.get_by_test_id(
        "registration-page-registration-button"
    ).click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    cours_elements = [
        page.get_by_test_id("courses-list-toolbar-title-text"),
        page.get_by_test_id("courses-list-empty-view-icon"),
        page.get_by_test_id("courses-list-empty-view-title-text"),
        page.get_by_test_id("courses-list-empty-view-description-text"),
    ]

    for element in cours_elements:
        expect(element).to_be_visible()

    page.wait_for_timeout(2000)
