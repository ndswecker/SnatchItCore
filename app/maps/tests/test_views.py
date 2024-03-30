from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def setUp(self):
        User = get_user_model()  # Get the custom user model
        self.user = User.objects.create_user(username="user", password="pass")
        self.client = Client()

    def test_capture_record_list_GET(self):
        self.client.login(username="user", password="pass")  # Log in the user
        response = self.client.get(reverse("maps:list_capture_records"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "maps/list_all.html")
