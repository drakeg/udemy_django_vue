from django.contrib import admin
from .models import JobOffer, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(JobOffer)