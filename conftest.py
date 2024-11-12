import pytest
import base64
import config
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, dict[str, int]]):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1480,
            "height": 1024,
        }
    }
