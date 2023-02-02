from model.pages.main_page import open_page, click_sign_in_button, \
    check_test_in_form, click_on_burger_menu


def test_open_desktop(setup_desktop_browser):
    open_page()
    click_sign_in_button()
    check_test_in_form()


def test_open_mobile(setup_mobile_browser):
    open_page()
    click_on_burger_menu()
    click_sign_in_button()
    check_test_in_form()