from django.test import TestCase
from django.http import HttpRequest
# Create your tests here.
#from isgkapp.views import top
from xml.etree.ElementInclude import include


class TopPageTest(TestCase):
    def test_include(self):
        print('test')
        return include('accounts.urls')
        