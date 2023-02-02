import pytest
from selene.support.shared import browser


@pytest.fixture
def setup_desktop_browser():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()


@pytest.fixture
def setup_mobile_browser():
    browser.config.window_width = 900
    browser.config.window_height = 940
    yield
    browser.quit()