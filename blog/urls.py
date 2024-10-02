from django.urls import path
from . import views
from .views import contact_view, success_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_page, name='success_page'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
