from django.contrib import admin
from django.urls import path, include
from . import views
from app.views import signin, signup, signout

urlpatterns = [
    # auth routes
    path('signup',signup,name="signup"),
    path('signin',signin,name="signin"),
    path('signout',signout,name="signout"),

    # app routes
    path('', views.home, name='home'),
    path('home', views.home, name='buddy-home'),
    
    # course routes
    path('courses', views.courses, name='buddy-courses'),
    path('view-course/<str:id>/', views.view_course, name='buddy-view-course'),
    path('register-course/<str:id>/', views.register_course, name='register-course'),
    
    path('blogs', views.blogs, name='blogs'),
    path('blog-page', views.blogs_page, name='blog-page'),
    path('events', views.events, name='events'),
    path('event', views.events_page, name='event'),
]

