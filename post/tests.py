from django.test import TestCase
import datetime

from django.utils import timezone
from post.models import Post, Comments

class PostMethodTests(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() should return False for post whose
        pub_date is in the future
        """
        future_post = Post(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() should return False for polls whose pub_date
        is older than 1 day
        """
        old_post = Post(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() should return True for polls whose pub_date
        is within the last day
        """
        recent_post = Post(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_post.was_published_recently(), True)