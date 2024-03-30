from django.test import SimpleTestCase
from django.urls import reverse, resolve

from maps import views


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse("maps:list_capture_records")
        self.assertEquals(resolve(url).func.view_class, views.ListCaptureRecordView)

    def test_detail_url_is_resolved(self):
        url = reverse("maps:detail_capture_record", args=[1])
        self.assertEquals(resolve(url).func.view_class, views.DetailCaptureRecordView)

    def test_create_url_is_resolved(self):
        url = reverse("maps:create_capture_record")
        self.assertEquals(resolve(url).func.view_class, views.CreateCaptureRecordView)
