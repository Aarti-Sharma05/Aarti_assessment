from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegisterAdmin(admin.ModelAdmin):
    field_display=['id','Name','Email','DOB','Phone_no']
