from django.shortcuts import render

# Create your views here.  I wrote code after this
from django.http import HttpResponse
from django.http import Http404 #if someone enters a id which does not exist so we use this
from .models import Employee


def home(request): #we are decalring home which takes in a request and return HttpResponse

    #return HttpResponse('Welcome Home') #we removed this line it was just basically to understand

    employees = Employee.objects.all()       #instead of previous commented statement to get details of employe using this statement
    return render(request, 'home.html', {'employees': employees})      #returned all the detail to home.html using dictionary

def employee_detail(request, employee_id):      # and also employee_detail which takes in a request and return HttpResonse
    #return HttpResponse(f'Employee ID: {employee_id}')     #did same here as done in previous function
    try:  #in try if employee id not found
        employee = Employee.objects.get(id=employee_id)       #this gives detail of specific employee using ids
    except Employee.DoesNotExist:
        raise Http404('Employee Not Found')
    return render(request,'employee_detail.html', {'employee': employee})  #here we ruturn employee details