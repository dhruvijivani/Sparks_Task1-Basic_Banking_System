from django.contrib import admin
from .models import user,transaction_details
# Register your models here.

admin.site.register(user)
admin.site.register(transaction_details)