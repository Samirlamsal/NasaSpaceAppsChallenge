from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from appchallenge import settings

urlpatterns=[
    path('Bookings/', views.form_view, name = 'form_view'),
    path('', views.home_view, name='home_view'),
    path('Explore/', views.explore_view, name='explore_view'),
    path('About/', views.about_view, name='about_view'),
]

urlpatterns = urlpatterns + staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
