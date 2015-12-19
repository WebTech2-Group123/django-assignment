from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Post


class PostFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='top_secret')

    def test_not_logged_in(self):
        c = Client()
        response = c.get('/posts/new')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/posts/new')

    def test_bad_submit(self):
        c = Client()

        # authenticate the user
        c.post('/accounts/login/', {'username': 'user', 'password': 'top_secret'})

        # bad request -> object not created
        c.post('/posts/new')
        self.assertEqual(len(Post.objects.all()), 0)

    def test_submit_post(self):
        c = Client()

        # authenticate the user
        c.post('/accounts/login/', {'username': 'user', 'password': 'top_secret'})

        # create a post
        response = c.post('/posts/new', {'title': 'Test Post', 'text': 'Some test text.'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.all()[0].title, 'Test Post')

    def test_show_posts(self):
        c = Client()

        # view all the posts
        response = c.get('/posts/')

        self.assertEqual(response.status_code, 200)
