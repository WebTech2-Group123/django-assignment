from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='top_secret')

    def test_save_and_retrieve_posts(self):
        post1 = Post()
        post1.title = 'Alex'
        post1.text = 'Sucks <3'
        post1.user = self.user
        post1.save()

        post2 = Post()
        post2.title = 'Davide'
        post2.text = 'Sucks even more <3'
        post2.user = self.user
        post2.save()

        posts = Post.objects.order_by('-creation_date')
        self.assertEqual(posts.count(), 2)

        self.assertEqual(posts[0], post2)
        self.assertEqual(posts[1], post1)


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
