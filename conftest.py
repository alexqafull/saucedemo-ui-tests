import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def setup_page(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.set_default_timeout(10000)