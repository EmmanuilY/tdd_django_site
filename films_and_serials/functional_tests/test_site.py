import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_films_and_serials_at_homepage(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    # She notices the page title and header mention to-do lists
    assert "Home" in browser.title





def test_jump_to_films_page(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    #Visitor click on "Films" link
    browser.find_element(By.LINK_TEXT,  "Go to Films").click()

    # She is taken to the "Films" page
    assert "Films" in browser.title


def test_jump_to_serials_page(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    #Visitor click on "Serials" link
    browser.find_element(By.LINK_TEXT,  "Go to Serials").click()

    # She is taken to the "Serials" page
    assert "Serials" in browser.title
