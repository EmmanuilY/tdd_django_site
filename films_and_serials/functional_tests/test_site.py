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
    assert "Home Page" in browser.title





def test_find_films_at_homepage(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    #She see name and poster of films
    films = browser.find_elements(By.CSS_SELECTOR, ".film")

    for film in films:
        # Ensure every film block has an image and a h2 title
        img = film.find_element(By.TAG_NAME, "img")
        title = film.find_element(By.TAG_NAME, "h3")

        # Test that the image has a src (url) and the title has some text.
        assert img.get_attribute("src") is not None
        assert title.text is not None

def test_find_serials_at_homepage(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    serials = browser.find_elements(By.CSS_SELECTOR, ".serial")

    for serial in serials:
        # Ensure every serial block has an image and a h2 title
        img = serial.find_element(By.TAG_NAME, "img")
        title = serial.find_element(By.TAG_NAME, "h3")

        # Test that the image has a src (url) and the title has some text.
        assert img.get_attribute("src") is not None
        assert title.text is not None

def test_jump_to_watchpage_and_find_film(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    #She see name and poster of films
    browser.find_element(By.CSS_SELECTOR, ".film").click()

    film = browser.find_element(By.CSS_SELECTOR, ".film_detail")
    # Ensure every film has an image and a h2 title
    img = film.find_element(By.TAG_NAME, "img")
    title = film.find_element(By.TAG_NAME, "h1")
    video = film.find_element(By.TAG_NAME, "video")
    source = video.find_element(By.TAG_NAME, "source")

    # Test that the image has a src (url) and the title has some text.
    assert img.get_attribute("src") is not None
    assert title.text is not None
    assert source.get_attribute("src") is not None

def test_jump_to_watchpage_and_find_serial(browser):
    # Visitor come to site
    browser.get("http://localhost:8000")

    #She see name and poster of films
    browser.find_element(By.CSS_SELECTOR, ".serial").click()

    film = browser.find_element(By.CSS_SELECTOR, ".serial_detail")
    # Ensure every film has an image and a h2 title
    img = film.find_element(By.TAG_NAME, "img")
    title = film.find_element(By.TAG_NAME, "h1")
    video = film.find_element(By.TAG_NAME, "video")
    source = video.find_element(By.TAG_NAME, "source")

    # Test that the image has a src (url) and the title has some text.
    assert img.get_attribute("src") is not None
    assert title.text is not None
    assert source.get_attribute("src") is not None





