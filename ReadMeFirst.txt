To run this project follow this steps:
1. Go to C:\Users\HARI-PC\Desktop\django_proj\mysite
2. Then in address bar type "cmd" which will open command prompt
3. Then in command prompt type "python manage.py runserver"
4. Then it will give you and address like "http://127.0.0.1:8000/" open that address in browser without closing command prompt
5. And you will see Employee database
6. To open admin panel append url in browser with "/admin" It's like "http://127.0.0.1:8000/admin" and type username: hari-pc and password: PASSWORD
7. Now here in admin panel you can manage operation over database like add, delete, see etc.

Thank you for having a look over this project.
developed by Vaibhav Bhawsar


Here it is all details how this project is created in my understanding

Through command promp in windows write command:

1. "pip3 install Django"   it will install django
2. "cd desktop"   	   it will move you to desktop
3. "mkdir django"   	   it will make dir django at desktop
4. "cd django"   	   it will move your to django folder
5. "django-admin startproject PROJECT_NAME" it will create project PROJECT_NAME
6. "cd mysite"             it will move to mysite folder
7. "python manage.py runserver" it will start server can be opened using address cmd prompt provides like http://127.0.0.1:8000/

Through pycharm community edition go to the link and see: "https://www.pragmaticlinux.com/2020/09/setup-and-debug-a-django-app-in-pycharm-community-edition/"
after setting up python project run this command in pycharm
1. "python manage.py startapp APP_NAME" it will create app APP_NAME
2. then in employees in models.py I have created look there your will get it.
3. after creating two classes in models.py we went to mysite/setting.py and in INSTALLED_APPS we added 'employees' in last
and save setting.py
4. next open models.py again and run a command "python manage.py makemigrations" which wil Create model AvailableJobs and Create model Employee
5. Then we will run "python manage.py showmigrations" and we found [ ] 0001_initial is unchecked like others so 
6. we will run next command "python manage.py migrate" it will show Applying employees.0001_initial... Ok
7. then again check using command "python manage.py showmigrations" now everything will be checked
8. Now in order to check using SQLite we downloaded SQLite 64 bit zip vesio from https://sqlitebrowser.org/dl/ and extract it to c:/programfile(x86) manually. And going in the folder we opened "DB Browser for SQLite.exe"
9. then in application we clicked "Open Database" and selected "C:\Users\HARI-PC\Desktop\django_proj\mysite\db.sqlite3
10. Now that we have made our migartion it's time to create our superuser.
11. So type "python manage.py createsuperuser"
	Username: leave blank to use hari-pc
	email: vaibhavbhawsar777@gmail.com
	Password: PASSWORD
	Password(again): PASSWORD
	superuser has been created.
12. launched the project in the browser using command again "python manage.py runserver"
browser will be opened and in url append url with /admin like http://127.0.0.1:8000/admin hit enter and then typed username: hari-pc adn password: PASSWORD and login we are succesfully logedin
13. now we will add employe table in there so 
14. came back to pycharm in employees/admin.py I wrote register Employee using some code see their in file
15. then rerun the server using cmd "python manage.py runserver" open browser and refresh that page and you found that in browser that Employees table.
16. now click over it and we found we do not have any employees so we added some by clicking on add employees 
17. at a point in between adding employees process we found that last name has dull in color which means it is optional as we use blank=True in defining this table.
18. after adding 3 employee we found that it show employee object and can able to fill Employee job so we register first Employee job in admin.py
19. In models.py we have created AvailableJob previous now we register it in admin.py check code there in admin.py
20. After doing this we rerun the browser using "python manage.py runserver" and refresh the page in browser and found we got a plus sign in Employee job and new table Available Jobss at home.
21. Now we will replace Employee object to do this we will define a function _str_(self) in Available jobs in model.py and list_display in admin.py and then ran the server again.
22. and then using browser we assign them their job.

23. Now next how to work with the url patterns.
24. edit the employees/view.py file
25. Here we will be creating our home page and employee detail page.
which defines a function and return a HttpResponse
26. then we changed the view as we wants using employees/migrations/views.py
27. then we changed the homepage using employees/mysite/urls.py
by importing view.py and creating 2 paths one for home page and other for viewing employee details.
28. next after saving all this work we refresh in the browser and in url just to confirm typed "127:0:0:1:8000/employee_detail/23"
which shows "Employee ID: 23" on browser page or can show detail for Employee ID: 23
29. Now some thing we changed the work done in step 28, 29 it was just basically to check how it runs 
30. So next in views we import models.py and through functions home and employee detail, we returned the employee details using dictionary. See in view.py for further clarifcation.
31. Next we create a folder named template in employees basically it is for html files. And created html file home.html and employee_detail.html in it
32. We solved a templates folder error because first I didnt added s to template while name a folder templates
33. now we edited home.html
34. then we have created employee.html
35. then we created base.html by using bootstrap which gave it an awesome look.

Thank you.
