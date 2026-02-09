from playwright.sync_api import Page, expect
import pytest

def test_index_page(page: Page):
    page.goto("http://localhost:3000/index.html")
    expect(page).to_have_title("Steal A Brainrot | The Ultimate Tool")
    expect(page.get_by_text("Status: Undetected")).to_be_visible()
    expect(page.get_by_role("link", name="Download Now")).to_be_visible()

def test_download_page(page: Page):
    page.goto("http://localhost:3000/download.html")
    expect(page.get_by_text("CHOOSE YOUR PLATFORM")).to_be_visible()
    expect(page.get_by_role("link", name="Windows")).to_be_visible()
    expect(page.get_by_role("link", name="Android")).to_be_visible()

def test_under_construction_page(page: Page):
    page.goto("http://localhost:3000/under-construction.html")
    expect(page.get_by_text("UNDER CONSTRUCTION")).to_be_visible()
    expect(page.get_by_text("69%")).to_be_visible()
