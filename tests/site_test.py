import pytest
import os
from playwright.sync_api import Page, expect

# Base URL for the local server
BASE_URL = "http://localhost:3000"

def test_index_page(page: Page):
    page.goto(f"{BASE_URL}/index.html")
    expect(page).to_have_title("Steal A Brainrot | The Ultimate Tool")
    expect(page.locator("h1")).to_contain_text("STEAL A BRAINROT")
    expect(page.get_by_role("link", name="Download Now")).to_be_visible()

def test_download_page(page: Page):
    page.goto(f"{BASE_URL}/download.html")
    expect(page).to_have_title("Download | Steal A Brainrot")
    expect(page.locator("h1")).to_contain_text("CHOOSE YOUR PLATFORM")

def test_navigation_header(page: Page):
    page.goto(f"{BASE_URL}/index.html")
    # These will be added in later steps, but we can write the tests now
    expect(page.get_by_role("link", name="Home", exact=True)).to_be_visible()
    expect(page.get_by_role("link", name="Download", exact=True)).to_be_visible()

    page.get_by_role("link", name="Download", exact=True).click()
    assert "download.html" in page.url

def test_under_construction(page: Page):
    page.goto(f"{BASE_URL}/under-construction.html")
    expect(page.locator("h1")).to_contain_text("UNDER CONSTRUCTION")
    expect(page.locator("text=69%")).to_be_visible()
