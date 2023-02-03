from django.contrib import admin
from .models import Customer, Models, Bookingdetails, Billing

# Register your models here.
admin.site.register(Customer)
admin.site.register(Models)
admin.site.register(Bookingdetails)
admin.site.register(Billing)
