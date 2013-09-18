from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(User):
    
    	#is_enduser = models.BooleanField(default=True)

	class Meta:
		proxy = True
		app_label = 'auth'
		verbose_name = 'Customer account'
		verbose_name_plural = 'Customer accounts'

class Staff(User):
	class Meta:
		proxy = True
		app_label = 'auth'
		verbose_name = 'Staff account'
		verbose_name_plural = 'Staff accounts'
