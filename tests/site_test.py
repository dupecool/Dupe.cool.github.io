import pytest
import re
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("path", [
    "/index.html",
    "/download.html",
    "/under-construction.html"
])
def test_navigation_header_presence(page: Page, path):
    page.goto(f"http://localhost:3000{path}")
    header = page.locator('nav')
    expect(header).to_be_visible()

    # Check logo in header using exact=True and limiting scope to header
    expect(header.get_by_text("STEAL A BRAINROT", exact=True)).to_be_visible()

def test_index_content(page: Page):
    page.goto("http://localhost:3000/index.html")
    expect(page.get_by_text("STATUS: UNDETECTED")).to_be_visible()
    expect(page.get_by_text("Sigma Level 100")).to_be_visible()
    expect(page.get_by_role("link", name="Download Now")).to_be_visible()

def test_navigation_links(page: Page):
    page.goto("http://localhost:3000/index.html")

    # Click DOWNLOAD in header
    page.locator('nav').get_by_role("link", name="DOWNLOAD").click()
    expect(page).to_have_url(re.compile(r"download\.html$"))

    # Click HOME in header
    page.locator('nav').get_by_role("link", name="HOME").click()
    expect(page).to_have_url(re.compile(r"(index\.html$|/$)"))

def test_download_to_construction_navigation(page: Page):
    page.goto("http://localhost:3000/download.html")
    # Click the Android card which links to under-construction.html
    page.get_by_text("Android").click()
    expect(page).to_have_url(re.compile(r"under-construction\.html$"))
