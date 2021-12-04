from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView, LogoutView
from todolist.views import CustomLoginView,RegisterPage
from django.urls import resolve 

# Create your tests here.

class UrlTestCase(SimpleTestCase):

    def test_login_url_resolved(self):
        '''Checking login page url'''
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)
    def test_register_url_resolved(self):
        url1 = reverse('register')
        self.assertEquals(resolve(url1).func.view_class, RegisterPage)# Create your tests here.
