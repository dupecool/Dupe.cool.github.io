from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Take screenshot of home page
        page.goto("http://localhost:3000/index.html")
        page.set_viewport_size({"width": 1280, "height": 800})
        page.screenshot(path="verification/home.png")

        # Take screenshot of download page
        page.goto("http://localhost:3000/download.html")
        page.screenshot(path="verification/download.png")

        browser.close()

if __name__ == "__main__":
    run()
