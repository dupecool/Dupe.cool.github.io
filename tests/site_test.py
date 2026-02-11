import pytest
import re
from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    page.goto("http://localhost:3000/index.html")
    expect(page).to_have_title(re.compile("Steal A Brainrot"))
    # Using a more robust selector that handles the span
    expect(page.locator("h1")).to_contain_text("STEAL A BRAINROT")

def test_navigation_to_download(page: Page):
    page.goto("http://localhost:3000/index.html")
    # There might be multiple "Download Now" links if I add a header
    page.get_by_role("link", name="Download Now").first.click()
    expect(page).to_have_url(re.compile("download.html"))
    expect(page.locator("h1")).to_contain_text("CHOOSE YOUR PLATFORM")

def test_navigation_back_home(page: Page):
    page.goto("http://localhost:3000/download.html")
    page.get_by_role("link", name="Back to Home").click()
    expect(page).to_have_url(re.compile("index.html"))

def test_under_construction_page(page: Page):
    page.goto("http://localhost:3000/download.html")
    page.get_by_role("link", name="Android").click()
    expect(page).to_have_url(re.compile("under-construction.html"))
    expect(page.locator("h1")).to_contain_text("UNDER CONSTRUCTION")
