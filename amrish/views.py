from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Create your views here.

url = "mongodb://localhost:27017"
client = MongoClient(url, server_api=ServerApi('1'))

db = client.myprobuddy
db_user = db.users
db_courses = db.courses


def index(request):
    return render(request, 'index.html')

def amrish(request):
    return render(request, 'home.html')

def members(request):
    return render(request, 'members.html')

def members_page(request):
    return render(request, 'members-page.html')

def freelancers(request):
    return render(request, 'freelancers.html')

def groups(request):
    return render(request, 'groups.html')

def group_profile(request):
    return render(request, 'group-profile.html')

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
    return render(request, 'courses.html',{'courses':db_courses.find()})

def create_courses(request):
    return render(request, 'courses.html')

def courses_page(request):
    return render(request, 'courses-page.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')

def blog(request):
    return render(request, 'blog.html')

def blog_page(request):
    return render(request, 'blog-page.html')

def events(request):
    return render(request, 'events.html')

def event(request):
    return render(request, 'event.html')
