from django.contrib import admin

# Register your models here. ( I wrote code after this)
from .models import Employee, AvailableJobs  #we added AvailableJobs later and rerun the server
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email_id', 'phone_num'] #list_display is predefined and in it are variable names defined in models.py classes
@admin.register(AvailableJobs)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']
