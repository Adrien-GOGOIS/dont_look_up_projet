from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto("http://127.0.0.1:8000/")

    page.get_by_label("Jusqu'au :").fill("2022-10-19")

    page.get_by_role("button", name="Recherche").click()
    page.wait_for_url("http://127.0.0.1:8000/")

    page.get_by_role("link", name="En savoir plus...").nth(1).click()
    page.wait_for_url("http://127.0.0.1:8000/asteroid/2252793/")

    page.get_by_role("button", name="Retour aux résultats").click()
    page.wait_for_url("http://127.0.0.1:8000/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
