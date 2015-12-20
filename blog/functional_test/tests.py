from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.admin import User


class PostTest(StaticLiveServerTestCase):
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
        save_button = self.browser.find_elements_by_css_selector('button[type=submit]')[0]
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


class ProfileTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        User.objects.create_user('admin', None, 'password123')

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def login(self, password):
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')
        username_field.send_keys('admin')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def test_edit_profile(self):
        self.browser.get(self.live_server_url + '/accounts/profile/edit')

        # login
        self.login('password123')

        # change name
        first_name_field = self.browser.find_element_by_name('first_name')
        last_name_field = self.browser.find_element_by_name('last_name')
        save_button = self.browser.find_elements_by_css_selector('button[type=submit]')[0]
        first_name_field.send_keys('first')
        last_name_field.send_keys('last')
        save_button.click()

        # check name
        user = User.objects.filter(username='admin').first()
        self.assertEqual(user.first_name, 'first')
        self.assertEqual(user.last_name, 'last')

    def test_change_password(self):
        self.browser.get(self.live_server_url + '/accounts/password/change/')

        # login
        self.login('password123')

        # change password
        old_field = self.browser.find_element_by_name('old_password')
        new_field = self.browser.find_element_by_name('new_password1')
        confirm_field = self.browser.find_element_by_name('new_password2')
        save_button = self.browser.find_elements_by_css_selector('button[type=submit]')[0]
        old_field.send_keys('password123')
        new_field.send_keys('newPass1')
        confirm_field.send_keys('newPass1')
        save_button.click()

        # logout
        self.browser.get(self.live_server_url + '/accounts/logout/')

        # profile page
        self.browser.get(self.live_server_url + '/accounts/profile/')

        # login
        self.login('newPass1')

        # should be in profile page
        self.assertTrue('/accounts/profile/' in self.browser.current_url)
