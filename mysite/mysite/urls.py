"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees import views     #I wrote this

urlpatterns = [
    path('admin/', admin.site.urls),
    # I wrote after this
    # here '' means it's a path for home page
    #and nextone is used to get employee_details from view
    path('', views.home, name='home'),
    path('employee_detail/<int:employee_id>', views.employee_detail, name='employee_detail'),
]
