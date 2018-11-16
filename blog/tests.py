from django.test import TestCase

# Create your tests here.
from datetime import datetime
from django.test.client import Client
from blog.models import BlogPost
from django.utils import timezone

class BlogPostTest(TestCase):
    def test_obj_create(self):
        BlogPost.objects.create(title='raw title',
                                body ='raw body',timestamp=timezone.now())
        self.assertEqual(1,BlogPost.objects.count())
        self.assertEqual('raw title',BlogPost.objects.get(id=1).title)
    def test_home(self):
        response = self.client.get('')
        self.failUnlessEqual(response.status_code,200)
    def test_slash(self):
        response = self.client.get('/post/new')
        self.assertIn(response.status_code,(301,302))

    def test_empty_create(self):
        response = self.client.get('/create/')
        self.assertIn(response.status_code,(301,302))
    def test_post_create(self):
        response = self.client.post('/create/',{
            'title':'post title',
            'body':'post body',
        })
        self.assertIn(response.status_code,(301,302))
        self.assertEqual(1,BlogPost.objects.count())
        self.assertEqual('post title',
                         BlogPost.objects.get(id=1).title)