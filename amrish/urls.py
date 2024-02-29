from django.contrib import admin
from django.urls import path, include
from . import views
from app.views import signin, signout

urlpatterns = [
    # auth routes
    path('amrish/signin',signin,name="signin"),
    path('amrish/signout',signout,name="signout"),

    # app routes
    path('', views.amrish, name='amrish'),
    path('home', views.amrish, name='home'),
    path('members', views.members, name='members'),
    path('members-page', views.members_page, name='members-page'),
    path('user-profile', views.members_page, name='user-profile'),
    path('freelancers', views.freelancers, name='freelancers'),
    path('groups', views.groups, name='groups'),
    path('group-profile', views.group_profile, name='group-profile'),
    path('courses', views.courses, name='courses'),
    path('create-courses', views.create_courses, name='create-courses'),
    path('courses-page', views.courses_page, name='courses-page'),
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'),
    path('blog', views.blog, name='blog'),
    path('blog-page', views.blog_page, name='blog-page'),
    path('events', views.events, name='events'),
    path('event', views.event, name='event'),
]

