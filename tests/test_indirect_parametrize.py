import pytest
from selene.support.shared import browser
from model.pages.main_page import open_page, click_sign_in_button, \
    check_test_in_form, click_on_burger_menu


@pytest.fixture(params=["1920*1080", "900*940"])
def window(request):
    if request.param == "1920*1080":
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == "900*940":
        browser.config.window_width = 900
        browser.config.window_height = 940


@pytest.mark.parametrize("window", ["1920*1080"], indirect=True)
def test_open_github_desktop(window):
    open_page()
    click_sign_in_button()
    check_test_in_form()


@pytest.mark.parametrize("window", ["900*940"], indirect=True)
def test_open_github_mobile(window):
    open_page()
    click_on_burger_menu()
    click_sign_in_button()
    check_test_in_form()