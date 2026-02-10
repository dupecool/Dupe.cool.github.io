import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="module")
def server():
    import subprocess
    import time
    process = subprocess.Popen(["python3", "-m", "http.server", "3000"])
    time.sleep(2)  # Wait for server to start
    yield "http://localhost:3000"
    process.terminate()

def test_index_page(page: Page, server):
    page.goto(f"{server}/index.html")
    expect(page).to_have_title("Steal A Brainrot | The Ultimate Tool")
    expect(page.get_by_role("heading", name="STEAL A BRAINROT")).to_be_visible()
    expect(page.get_by_text("Status: Undetected")).to_be_visible()
    expect(page.get_by_role("link", name="Download Now")).to_be_visible()

def test_download_page(page: Page, server):
    page.goto(f"{server}/download.html")
    expect(page).to_have_title("Download | Steal A Brainrot")
    expect(page.get_by_role("heading", name="CHOOSE YOUR PLATFORM")).to_be_visible()
    expect(page.get_by_role("link", name="Windows")).to_be_visible()

def test_under_construction_page(page: Page, server):
    page.goto(f"{server}/under-construction.html")
    expect(page).to_have_title("Under Construction | Steal A Brainrot")
    expect(page.get_by_role("heading", name="UNDER CONSTRUCTION")).to_be_visible()
    expect(page.get_by_text("69%")).to_be_visible()

def test_navigation(page: Page, server):
    page.goto(f"{server}/index.html")
    page.get_by_role("link", name="Download Now").click()
    expect(page).to_have_url(f"{server}/download.html")

    # Click Home link in nav (exact match)
    page.get_by_role("link", name="Home", exact=True).click()
    expect(page).to_have_url(f"{server}/index.html")
