from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.talabat.com/uae/restaurants/1252/business-bay")
    page.locator("[data-test=\"rest-search-box\"]").click()
    page.locator("[data-test=\"rest-search-box\"]").press("CapsLock")
    page.locator("[data-test=\"rest-search-box\"]").fill("S")
    page.locator("[data-test=\"rest-search-box\"]").press("CapsLock")
    page.locator("[data-test=\"rest-search-box\"]").fill("Sushi")
    page.locator("[data-test=\"rest-search-box\"]").press("Enter")
    page.get_by_role("link", name="Sushi Workshop, Bao & Katsu Sushi Workshop, Bao & Katsu Sushi, Japanese, Asian Very good Within 35 mins Delivery: 9.00 Min: 10.00 Talabat Discounts Discounts Live Tracking Contactless drop-off").click()
    page.get_by_text("Build Your Own Katsu Curry").first.click()
    page.get_by_role("img", name="Alert Close Button Image").click()
    page.locator(".currency").first.click()
    page.get_by_role("img", name="Alert Close Button Image").click()
    page.get_by_text("Build your own Katsu curry! Select fresh rice, protein and toppings").first.click()
    page.locator("div").filter(has_text="Your Choice Of:(Choose 1)").first.click()
    page.get_by_role("img", name="Alert Close Button Image").click()
    page.get_by_test_id()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
