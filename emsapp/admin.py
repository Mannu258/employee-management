from django.contrib import admin
from . models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("id",'name')

admin.site.register(Employee)
admin.site.register(Department,MemberAdmin)
admin.site.register(Role,MemberAdmin)
