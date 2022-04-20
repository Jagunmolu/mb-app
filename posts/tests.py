from turtle import title
from urllib import response
from django.test import TestCase
from django.urls import reverse

from .models import Post

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')


class PostModelTest(TestCase):
    
    def setUp(self) -> None:
        Post.objects.create(title='This is a Test!', description='This is a Test Description!', text='This is a Test Text!')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        output = f'{post.title}'
        self.assertEqual(output, 'This is a Test!')

    def test_description_content(self):
        post = Post.objects.get(id=1)
        output = f'{post.description}'
        self.assertEqual(output, 'This is a Test Description!')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        output = f'{post.text}'
        self.assertEqual(output, 'This is a Test Text!')