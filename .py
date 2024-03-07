# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# url = "mongodb+srv://pro_user:rkwyrUiPnjjBsssg@cluster0.edxis.mongodb.net/?retryWrites=true&w=majority"

# client = MongoClient(url, server_api=ServerApi('1'))

# db = client.mpb
# db_user = db.users
# db_courses = db.courses
# db_events = db.events

# db_events.delete_many(filter={})

# import datetime
# print(str(datetime.datetime.now()).replace(":","").replace("-","").replace(" ","").split('.')[0][:-2])
# def convert_event_datetime(date_string, time_string):
#     def format_date(date_string):
#         mon=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
#         date=str(date_string).replace(" – "," ").replace(",","").lower().split(" ")
#         if date[2] not in mon:
#             date[0]=mon.index(date[0])+1
#             date[3]=mon.index(date[3])+1
#         elif date[0] in mon and date[2] in mon:
#             date[0]=mon.index(date[0])+1
#             date[2]=mon.index(date[2])+1    
#         start_date = int(str(date[-1])+str(date[0])+str(date[1]))
#         end_date = int(str(date[-1])+str(date[2])+str(date[3]))
#         return start_date, end_date
    
#     def format_time(time_string):
#         time_string=str(time_string)
#         time_string=time_string.split(" - ")
#         time_string[0]=time_string[0].split(" ")
#         if time_string[0][1]=="pm":
#             time_string[0][0]=str(int(time_string[0][0].split(":")[0])+12)+time_string[0][0].split(":")[1]
#         else:
#             time_string[0][0]=time_string[0][0].split(":")[0]+time_string[0][0].split(":")[1]
#         time_string[1]=time_string[1].split(" ")
#         if time_string[1][1]=="pm":
#             time_string[1][0]=str(int(time_string[1][0].split(":")[0])+12)+time_string[1][0].split(":")[1]
#         else:
#             time_string[1][0]=time_string[1][0].split(":")[1]+time_string[1][0].split(":")[1]
        
#         if len(time_string[0][0])==3:
#             time_string[0][0]="0"+time_string[0][0]
        
#         start_time=time_string[0][0]
#         end_time=time_string[1][0]

#         return start_time, end_time    
    
#     start_time,end_time=format_time(time_string)
#     start_date,end_date=format_date(date_string)
    
#     start = int(str(start_date)+str(start_time))
#     end = int(str(end_date)+str(end_time))
    
#     return start, end
    
# print(convert_event_datetime(date_string="Feb 27 – Mar 2, 2023",time_string="9:30 am - 6:00 pm"))

# lu=str(datetime.datetime.now()).replace(":","").replace(".","").replace("-","").replace(" ","")
# print(lu)

# db_courses.insert_one(
#     {
#         "_id": "65dc35e37f758aec4d972360",
#         "oid": "path-to-develop-a-webapplication-7-weeks",
#         "course_title": "Full Stack Developer",
#         "course_description": "Entrepreneurship is the pursuit of creating value through innovative ventures. Entrepreneurs embrace risk, manage resources efficiently, and adapt to changing markets. Leadership, persistence, and market insight are essential for success. It involves turning vision into reality by identifying opportunities and solving problems.",
#         "course_price": 4000,
#         "course_duration": "7 Weeks",
#         "course_category": "Development",
#         "course_type": "free",
#         "course_author": "Amrish",
#         "course_enrolled": 420,
#         "course_about": "Entrepreneurship is the dynamic process of identifying opportunities, marshaling resources, and creating value by bringing together innovative ideas, people, and capital. It is the pursuit of turning vision into reality, often involving the initiation and management of a new business venture. Entrepreneurs are individuals who possess a unique set of skills, including creativity, risk-taking, resilience, and a keen business acumen. They are driven by a passion to solve problems, meet market needs, or introduce groundbreaking innovations. Entrepreneurship is not limited to the establishment of new businesses; it also encompasses the ability to foster growth and adaptability within existing enterprises.",
#         "course_for": "Learners design and justify small-scale positive interventions to enhance specific aspects of their personal wellbeing based on the skills acquired in each course of the specialization. Personal reflections are implemented provide learners with the skills to impact their personal and professional lives.",
#         "course_skills": [
#             "Create storyboards to come up with ideas about solutions to user needs.",
#             "Build paper prototypes to create interactive designs.",
#             "Create wireframes on paper and digitally in the design tool Figma.",
#             "Design low-fidelity prototypes in Figma."
#         ],
#         "course_requirements": "To be successful in this course, you should complete the previous two courses in this certificate program, or have an ability to conduct user research to inform the creation of empathy maps, personas, user stories, user journey maps, problem statements, and value propositions. You will also need paper and a pen or pencil.",
#         "course_certificate": "Yes",
#         "course_language": "English",
#         "course_level": "Advanced",
#         "course_inner_title": "Path to Develop a WebApplication",
#         "course_rating": 4.3,
#         "course_contains": "20 Lessons",
#         "course_tags": "free development fullstack",
#         "course_image": "url",
#         "course_about_image": "url"
#     }
# )


# db_courses.insert_one(
#     {"_id":{"$oid":"65e0d21e1258a15cf1ba1774"},
#      "oid":"django-web-development-course-prerequisites-9-weeks",
#      "course_title":"Full Stack Django Developer",
#      "course_description":"Entrepreneurship is the pursuit of creating value through innovative ventures. Entrepreneurs embrace risk, manage resources efficiently, and adapt to changing markets. Leadership, persistence, and market insight are essential for success. It involves turning vision into reality by identifying opportunities and solving problems.","course_price":"3500","course_duration":"9 weeks","course_category":"Development","course_type":"Paid","course_author":"Abishek","course_enrolled":"420","course_about":"Django is a high-level Python web framework that facilitates full-stack development. It includes an ORM for database management, URL routing, and templating for the front end. Django follows the Model-View-Controller (MVC) architectural pattern, providing a comprehensive solution for building robust and scalable web applications. With built-in security features and an admin panel, Django simplifies both front-end and back-end development tasks, making it an ideal choice for developers aiming to create full-stack applications efficiently.","course_for":"Django is suitable for web developers, Python developers, beginners in web development, software engineers, entrepreneurs, startups, students, and programming enthusiasts looking to build robust and scalable web applications using Python.","course_skills":"By completing a Django course, you can gain the following skills:\r\n\r\n1. **Full-Stack Web Development:** Acquire proficiency in both front-end (HTML, CSS, JavaScript) and back-end (Python, Django) development for building complete web applications.\r\n\r\n2. **Database Management:** Learn to work with databases using Django's built-in Object-Relational Mapping (ORM) for efficient data handling.\r\n\r\n3. **MVC Architecture:** Understand and implement the Model-View-Controller architectural pattern for well-organized and scalable code.\r\n\r\n4. **Security Practices:** Gain knowledge of best practices for securing web applications, as Django includes built-in security features.\r\n\r\n5. **Efficient Routing and Templating:** Master URL routing and templating to create dynamic and user-friendly interfaces.\r\n\r\n6. **Deployment Strategies:** Learn how to deploy Django applications and manage the deployment process.\r\n\r\n7. **Admin Panel Usage:** Utilize Django's admin panel for easy content management and application administration.\r\n\r\n8. **Version Control:** Familiarize yourself with version control systems, enhancing collaboration and code management.\r\n\r\nThese skills collectively empower you to develop, deploy, and maintain robust web applications using Django.","course_requirements":"To undertake a Django course, you typically need the following prerequisites:\r\n\r\n1. **Basic Programming Knowledge:** Familiarity with programming fundamentals, especially in Python, is beneficial.\r\n\r\n2. **HTML, CSS, and JavaScript Basics:** Understanding the basics of front-end technologies such as HTML, CSS, and JavaScript will be helpful for full-stack development.\r\n\r\n3. **Command Line Skills:** Proficiency in using the command line interface (CLI) for tasks like running scripts and managing projects is advantageous.\r\n\r\n4. **Text Editor or IDE Familiarity:** Experience with a text editor (e.g., VS Code, Sublime Text) or an Integrated Development Environment (IDE) will aid in coding exercises.\r\n\r\n5. **Internet Connection:** A stable internet connection is necessary for accessing course materials, downloading software, and participating in online discussions.\r\n\r\n6. **Computer Setup:** Ensure your computer meets the hardware and software requirements for running Django and its associated tools.\r\n\r\n7. **Optional: Database Basics:** Some courses may assume basic knowledge of databases. If not, you may learn this during the course.\r\n\r\nAlways check the specific requirements outlined by the course provider to ensure you meet all prerequisites and have the necessary tools for a smooth learning experience.","course_certificate":"Yes","course_language":"English","course_level":"Advanced","course_inner_title":"Django Web Development Course Prerequisites","course_rating":"5","course_contains":"14","course_tags":"django python web","course_image":"url","course_about_image":"url"}
# )

# i=db_courses.find(filter={"oid":"django-web-development-course-prerequisites-9-weeks"}):
# arr=str(i['course_requirements'])
# arr=arr.split("<li>")
# for i in range(len(arr)):
#     arr[i]=arr[i].split("</li>")[0]

# db_courses.find_one_and_update(filter={"oid":"django-web-development-course-prerequisites-9-weeks"},update={"$set":{"course_skills":arr}})
