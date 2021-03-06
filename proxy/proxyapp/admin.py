from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Customer,Staff

class StaffAdmin(UserAdmin):
	
	def queryset(self,request):
		qs = super(UserAdmin,self).queryset(request)
		qs = qs.filter(Q(is_staff=True) | Q(is_superuser=True))
		return qs

class CustomerAdmin(StaffAdmin):
	
	def queryset(self,request):
		qs = super(UserAdmin,self).queryset(request)
		qs = qs.exclude(Q(is_staff=True) | Q(is_superuser=True))
		return qs

admin.site.unregister(User)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Customer,CustomerAdmin)
