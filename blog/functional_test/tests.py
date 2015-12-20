from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.admin import User


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        User.objects.create_user('admin', None, 'password123')

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def test_login_and_post(self):
        # add post page
        self.browser.get(self.live_server_url + '/posts/new')

        # login
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')
        username_field.send_keys('admin')
        password_field.send_keys('password123')
        password_field.send_keys(Keys.RETURN)

        # add post
        title_field = self.browser.find_element_by_name('title')
        text_field = self.browser.find_element_by_name('text')
        save_button = self.browser.find_elements_by_css_selector('input[type=submit]')[0]
        title_field.send_keys('lorem')
        text_field.send_keys('ipsum 123')
        save_button.click()

        # posts page
        first_post = self.browser.find_element_by_css_selector('.container>.panel')
        title = first_post.find_element_by_class_name('panel-heading').text
        text = first_post.find_element_by_class_name('panel-body').text
        author = first_post.find_element_by_class_name('panel-footer').text
        self.assertEqual('lorem', title)
        self.assertEqual('ipsum 123', text)
        self.assertTrue('@admin' in author)
