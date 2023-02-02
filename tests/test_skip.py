import pytest
from model.pages.main_page import open_page, click_sign_in_button, \
    check_test_in_form, click_on_burger_menu
from selene.support.shared import browser


@pytest.mark.parametrize("width, height", [pytest.param(1900, 1080), pytest.param(900, 940)])
def test_open_github_desktop(width, height):
    if width == 900:
        pytest.skip(reason="Пропустить, если разрешение экрана под мобилку")
    browser.config.window_width = width
    browser.config.window_height = height
    open_page()
    click_sign_in_button()
    check_test_in_form()


@pytest.mark.parametrize("browser_width, browser_height", [pytest.param(1900, 1080), pytest.param(900, 940)])
def test_open_github_mobile(browser_width, browser_height):
    if browser_width == 1900:
        pytest.skip(reason="Пропустить, если разрешение экрана под десктоп")
    browser.config.window_width = browser_width
    browser.config.window_height = browser_height
    open_page()
    click_on_burger_menu()
    click_sign_in_button()
    check_test_in_form()