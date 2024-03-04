from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from django.contrib.auth.decorators import user_passes_test
from app.views import db_user, db_courses, db_blogs

def is_buddy(user):
    return user.groups.filter(name='buddy').exists() 

@user_passes_test(is_buddy)
def home(request):
    return render(request, 'buddy/home.html')

@user_passes_test(is_buddy)
def courses(request):
    courses = {}
    for i in db_courses.find():
        courses[i['oid']] = {"course_category":i['course_category'],
            "course_title":i['course_title'],
            "course_rating":i['course_rating'],
            "course_contains":i['course_contains'],
            "course_enrolled":i['course_enrolled'],
            "course_author":i['course_author'],
            "course_price":i['course_price'],
            "course_image":i['course_image'],
            "course_duration":i['course_duration']
        }
    return render(request, 'buddy/courses.html',{'courses':db_courses.find()})

@user_passes_test(is_buddy)
def view_course(request,id):
    context={'course':db_courses.find_one({"oid":id})}
    return render(request,'buddy/courses-page.html',context)

@user_passes_test(is_buddy)
def register_course(request,id):
    print(id)
    db_user.find_one_and_update({"username":request.user.username},{"$push":{"courses":id}})
    context={'course':db_courses.find_one({"oid":id})}
    return render(request,'buddy/courses-page.html',context)

@user_passes_test(is_buddy)
def blogs(request):
    return render(request, 'buddy/blog.html')

@user_passes_test(is_buddy)
def blogs_page(request):
    return render(request, 'buddy/blog-page.html')

@user_passes_test(is_buddy)
def events(request):
    return render(request, 'buddy/events.html')

@user_passes_test(is_buddy)
def events_page(request):
    return render(request, 'buddy/event.html')
