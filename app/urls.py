from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # auth routes
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('ajaxsigningin', views.ajaxsigningin, name='ajaxsigningin'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    
    path('courses', views.courses, name='courses'),
    path('view-course/<str:id>/', views.view_course, name='view-course'),
    
    path('blogs', views.blogs, name='blogs'),
    path('blogs-page', views.blog_page, name='blogs-page'),

    path('events', views.events, name='events'),
    path('events-page', views.event_page, name='events-page'),
    
    path('trial', views.trial, name='trial'),
    path('c_data', views.c_data, name='c_data'),
]

