import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewUserTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_register_new_user(self):
        # User goes to the registration page
        self.browser.get(self.live_server_url + '/registration')


        # User types his username into the username field
        username_field = self.browser.find_element(By.NAME,'username')
        username_field.send_keys('newuser')
        # User types his email into the email field
        email_field = self.browser.find_element(By.NAME,'email')
        email_field.send_keys('newuser@example.com')
        # User types his password into the password field
        password_field = self.browser.find_element(By.NAME, 'password1')
        password_field.send_keys('mypassword123BB$')
        # User types his password into the password confirmation field
        password_confirm_field = self.browser.find_element(By.NAME, 'password2')
        password_confirm_field.send_keys('mypassword123BB$')


        # User clicks the register button
        register_button = self.browser.find_element(By.CSS_SELECTOR, 'form button')
        register_button.click()
        # User sees a message that registration was successful
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Registration successful', body.text)
