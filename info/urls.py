from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^news(?:/.*)?$', views.news, name='news'),
    re_path(r'^management(?:/.*)?$', views.management, name='management'),
    path('management/<int:id>/', views.director_detail, name='director_detail'),
    re_path(r'^activities(?:/.*)?$', views.activities, name='activities'),
    re_path(r'^contacts(?:/.*)?$', views.contacts, name='contacts'),
]
