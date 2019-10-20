from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

class JobOffer(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="joboffers")
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title