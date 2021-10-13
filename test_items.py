import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_presence(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector("qbutton.btn-add-to-basket"), "'Add to basket' button is missing"
