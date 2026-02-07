from playwright.sync_api import sync_playwright, expect
import pytest
import subprocess
import time
import os

@pytest.fixture(scope="module", autouse=True)
def server():
    proc = subprocess.Popen(["python3", "-m", "http.server", "3001"])
    time.sleep(1)
    yield
    proc.terminate()

def test_index_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:3001/index.html")
        expect(page.locator("h1")).to_contain_text("STEAL A BRAINROT")
        expect(page.get_by_role("link", name="Download Now")).to_be_visible()
        browser.close()

def test_download_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:3001/download.html")
        expect(page.locator("h1")).to_contain_text("CHOOSE YOUR PLATFORM")
        browser.close()

def test_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:3001/index.html")
        page.get_by_role("link", name="Download", exact=True).click()
        expect(page).to_have_url("http://localhost:3001/download.html")
        browser.close()
