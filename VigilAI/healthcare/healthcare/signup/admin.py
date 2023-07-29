from django.contrib import admin
from signup.models import Signup
class ServiceAdmin(admin.ModelAdmin):
    list_display=('name','token')
admin.site.register(Signup,ServiceAdmin)
# Register your models here.
