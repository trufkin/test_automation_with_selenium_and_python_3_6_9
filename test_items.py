import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_presence(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    print(add_to_basket_button)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), "'Add to basket' button is missing"
