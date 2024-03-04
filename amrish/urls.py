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
    path('home', views.home, name='amrish-home'),
    
    path('courses', views.courses, name='amrish-courses'),
    path('view-course/<str:id>/', views.courses_page, name='amrish-view-course'),
    path('create-course', views.create_course, name='amrish-create-course'),
    path('course-enrolled', views.course_enrolled, name='amrish-course-enrolled'),
    
    path('blogs', views.blogs, name='amrish-blogs'),
    path('blogs-page', views.blogs_page, name='amrish-blogs-page'),
    path('blogs-create', views.blogs_create, name='blogs-create'),

    path('events', views.events, name='amrish-events'),
    path('events-page', views.events_page, name='amrish-events-page'),
    path('events-registered', views.evens_registered, name='events-registered'),
]

