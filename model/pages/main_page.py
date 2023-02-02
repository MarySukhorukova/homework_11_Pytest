from selene import have
from selene.support.shared import browser


def open_page():
    browser.open('https://github.com/')


def click_sign_in_button():
    browser.element('[href="/login"]').click()


def check_test_in_form():
    assert browser.element('[for="login_field"]').should(have.text("Username or email address"))


def click_on_burger_menu():
    browser.element('.Button-label > div:first-child').click()