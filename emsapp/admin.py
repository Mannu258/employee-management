from django.contrib import admin
from . models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("first_name",'last_name','dep','role')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,MemberAdmin)
admin.site.register(Role,MemberAdmin)
