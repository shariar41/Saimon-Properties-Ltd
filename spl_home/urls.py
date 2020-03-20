from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="site-home"),
    path('about/', views.about, name="site-about"),
    path('ongoing_projects/', views.ongoing_projects, name="site-ongoing-projects"),
    path('upcoming_projects/', views.upcoming_projects, name="site-upcoming-projects"),
    path('completed_projects/', views.completed_projects, name="site-completed-projects"),
    path('contact/', views.contact, name="site-contact")
]