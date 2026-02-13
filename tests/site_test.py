import pytest
from playwright.sync_api import Page, expect
import os

# Ensure verification directory exists locally
VERIFICATION_DIR = "verification"
os.makedirs(VERIFICATION_DIR, exist_ok=True)

BASE_URL = "http://localhost:3000"

def test_homepage(page: Page):
    page.goto(f"{BASE_URL}/index.html")
    expect(page).to_have_title("Steal A Brainrot | The Ultimate Tool")

    # Check for main elements using specific selectors
    expect(page.get_by_role("heading", name="STEAL A BRAINROT")).to_be_visible()
    expect(page.get_by_text("Status: Undetected")).to_be_visible()

    # Take screenshot
    page.screenshot(path=os.path.join(VERIFICATION_DIR, "homepage.png"))

def test_download_page(page: Page):
    page.goto(f"{BASE_URL}/download.html")
    expect(page).to_have_title("Download | Steal A Brainrot")

    # Check for platform choices
    expect(page.get_by_role("heading", name="CHOOSE YOUR PLATFORM")).to_be_visible()
    expect(page.get_by_text("Windows")).to_be_visible()
    expect(page.get_by_text("Android")).to_be_visible()

    # Take screenshot
    page.screenshot(path=os.path.join(VERIFICATION_DIR, "download.png"))

def test_under_construction_page(page: Page):
    page.goto(f"{BASE_URL}/under-construction.html")
    expect(page).to_have_title("Under Construction | Steal A Brainrot")

    # Check for progress bar
    expect(page.get_by_text("Optimization Progress")).to_be_visible()
    expect(page.get_by_text("69%")).to_be_visible()

    # Take screenshot
    page.screenshot(path=os.path.join(VERIFICATION_DIR, "under_construction.png"))

def test_navigation(page: Page):
    page.goto(f"{BASE_URL}/index.html")

    # Click download in nav
    page.locator('nav').get_by_role("link", name="Download").click()
    expect(page).to_have_url(f"{BASE_URL}/download.html")

    # Click back to home
    page.locator('nav').get_by_role("link", name="Home").click()
    expect(page).to_have_url(f"{BASE_URL}/index.html")
