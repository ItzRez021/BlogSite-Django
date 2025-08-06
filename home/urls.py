from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('projects/',views.ProjectsView.as_view(),name='projects'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('newsletter/',views.NewsLetterView.as_view(),name='newsletter'),
    path('Blog-Detail/<int:pk>/',views.BlogDetailView.as_view(),name='blog-detail'),
]