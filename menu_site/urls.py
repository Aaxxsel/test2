from django.urls import path

from menu_site.views import *

urlpatterns = [
    path('', index, name='home'),
    path('tests/', show_tests, name='tests_list'),
    path('tests/<slug:slug>/', test_detail, name='test_detail'),
]
