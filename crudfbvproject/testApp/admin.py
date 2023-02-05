from django.contrib import admin
from testApp.models import EmployeeForm

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(EmployeeForm,EmployeeAdmin)
