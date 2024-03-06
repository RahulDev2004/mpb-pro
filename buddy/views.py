from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from django.contrib.auth.decorators import user_passes_test
from app.views import db_users, db_courses, db_blogs

def is_buddy(user):
    return user.groups.filter(name='buddy').exists()

@user_passes_test(is_buddy)
def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='amrish').exists():return redirect ("amrish-home")
    else:
        return redirect("login")
    def get_last_course():
        last_course={}
        t=0
        for i in db_courses.find():
            if t<i["last_update"]:
                t=i["last_update"]
                last_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
        return last_course
    
    def get_popular_course():
        popular_course={}
        t=0
        for i in db_courses.find():
            if t<int(i["course_enrolled"]):
                t=int(i["course_enrolled"])
                popular_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
        return popular_course
    
    popular_course = get_popular_course()
    last_course = get_last_course()
    return render(request, 'buddy/home.html',{"last_course":last_course,"popular_course":popular_course})

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
    user_course=db_users.find_one({"username":request.user.username})['courses']
    if id in user_course:
        print("Already Enrolled")
    else:
        db_users.find_one_and_update({"username":request.user.username},{"$push":{"courses":id}})
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
