from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.views import db_users, db_courses, db_events,db_blogs, timenow, convert_event_datetime
import datetime
# Create your views here.

def is_amrish(user):
    return user.groups.filter(name='amrish').exists()

def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='buddy').exists():return redirect ("buddy-home")
    else:return redirect("signin")
    # def get_last_course():
    #     last_course={}
    #     t=0
    #     for i in db_courses.find():
    #         if t<i["last_update"]:
    #             t=i["last_update"]
    #             last_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
    #     return last_course
    
    # def get_popular_course():
    #     popular_course={}
    #     t=0
    #     for i in db_courses.find():
    #         if t<int(i["course_enrolled"]):
    #             t=int(i["course_enrolled"])
    #             popular_course={"course_title":i["course_title"],"course_image":i["course_image"],"course_rating":i["course_rating"],"course_category":i["course_category"],"course_contains":i["course_contains"],"course_enrolled":i["course_enrolled"],"course_author":i["course_author"],"course_price":i["course_price"],"oid":i["oid"]}
    #     return popular_course
    
    # popular_course = get_popular_course()
    # last_course = get_last_course()
    # return render(request, 'amrish/home.html',{"last_course":last_course,"popular_course":popular_course})
    return render(request, 'amrish/home.html')

@user_passes_test(is_amrish)
def courses(request):
    return render(request, 'amrish/courses.html',{'courses':db_courses.find()})


@user_passes_test(is_amrish)
def create_course(request):
    return render(request, 'amrish/courses-create.html')

def add_course(request):
    course_about=str(request.POST.get('course_about')).strip().replace("\n","").split("<br>")
    course={
        "oid": str(request.POST.get("course_inner_title")).replace(" ","-").lower()+"-"+str(request.POST.get("course_duration")).replace(" ","-").lower(),
        "course_category": request.POST.get("course_category"),
        "course_title": request.POST.get("course_title"),
        "course_rating": request.POST.get("course_rating"),
        "course_lessons": request.POST.get("course_lessons"),
        "course_enrolled": request.POST.get("course_enrolled"),
        "course_author": request.POST.get("course_author"),
        "course_about": course_about,
        "course_for": request.POST.get("course_for"),
        "course_skills": request.POST.get("course_skills"),
        "course_requirements": request.POST.get("course_requirements"),
        "course_price": request.POST.get("course_price"),
        "course_level": request.POST.get("course_level"),
        "course_duration": request.POST.get("course_duration"),
        "course_language": request.POST.get("course_language"),
        "course_certificate": request.POST.get("course_certificate"),
        "course_type": request.POST.get("course_type"),
        "course_inner_title": request.POST.get("course_inner_title"),
        "course_tags": request.POST.get("course_tags"),
        "course_image": "url",
        "course_about_image": "url",
        "last_updated": timenow()
    }
    db_courses.insert_one(course)

def edit_course(request,id):
    context={'course':db_courses.find_one({"oid":id})}
    return render(request,'amrish/courses-edit.html',context)

@user_passes_test(is_amrish)
def courses_page(request,id):
    context={'course':db_courses.find_one({"oid":id})}
    return render(request,'amrish/courses-page.html',context)

@user_passes_test(is_amrish)
def course_enrolled(request):
    
    return render(request, 'amrish/courses-enrolled.html')

@user_passes_test(is_amrish)
def blogs(request):
    return render(request, 'amrish/blogs.html')

@user_passes_test(is_amrish)
def blogs_page(request):
    return render(request, 'amrish/blogs-page.html')

@user_passes_test(is_amrish)
def blogs_create(request):
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['content']
        db_blogs.insert_one({"title":title,"content":content})
        return redirect('blogs')
    else:
        return render(request, 'amrish/blogs-create.html')

@user_passes_test(is_amrish)
def events(request):
    # events_={}
    # for i in db_events.find():
    #     oid=str(str(i["event_title"])+str(i["event_date"])).replace(" ","-").lower()
    #     events_[oid]={"event_date":i["event_date"],"event_title":i["event_title"],"event_location":i["event_title_location"],"event_organizer":i["event_organization_name"],"event_venue":i["event_venue_place"],"event_price":i["event_price"],"event_venue_location":i["event_venue_location"],"event_venue_phone":i["event_venue_phone"],"event_organizer_email":i["event_organizer_email"],"event_phone":i["event_phone"],"event_website":i["event_website"],"event_location_map":i["event_location_map"]}
    return render(request, 'amrish/events.html', {'events':db_events.find()})

@user_passes_test(is_amrish)
def create_event(request):
    return render(request, 'amrish/events-create.html')

def add_event(request):
    event_about=str(request.POST.get('event_about')).strip().replace("\n","").split("<br>")
    event_map = str(request.POST.get('event_location_map')).strip().split("src=")[1].split(" ")[0].replace('"','')
    start,end=convert_event_datetime(date_string=str(request.POST.get('event_title_date')).strip(),time_string=str(request.POST.get('event_timing')).strip())
    if(str(request.POST.get('event_title')).strip()!=None):
        event={
            "oid":str(str(request.POST.get('event_title')).strip()+"-"+str(request.POST.get('event_date')).strip()).replace(" ","-").replace(",","-").lower(),
            "event_title":str(request.POST.get('event_title')).strip(),
            "event_title_date":str(request.POST.get('event_title_date')).strip(),
            "event_title_location":str(request.POST.get('event_title_location')).strip(),
            "event_organization_name":str(request.POST.get('event_organization_name')).strip(),
            "event_about":event_about,
            "event_price":int(str(request.POST.get('event_price')).strip()),
            "event_date":str(request.POST.get('event_date')).strip(),
            "event_timing":str(request.POST.get('event_timing')).strip(),
            "event_organizer_email":str(request.POST.get('event_organizer_email')).strip(),
            "event_phone":str(request.POST.get('event_phone')).strip(),
            "event_website":str(request.POST.get('event_website')).strip(),
            "event_venue_place":str(request.POST.get('event_venue_place')).strip(),
            "event_venue_location":str(request.POST.get('event_venue_location')).strip(),
            "event_venue_phone":str(request.POST.get('event_venue_phone')).strip(),
            "event_location_map":event_map,
            "event_start":start,
            "event_end":end,
            "event_dead":False,
            "registered":[],
        }
        # print(event)
        db_events.insert_one(event)
        return HttpResponse("Event Added")
    else:return HttpResponse("Event Not Added")

@user_passes_test(is_amrish)
def events_page(request,id):
    print(db_events.find_one({"oid":id})["event_about"])
    event={'event':db_events.find_one({"oid":id})}
    return render(request, 'amrish/events-page.html',event)

def evens_registered(request):
    return render(request, 'amrish/events-registered.html')