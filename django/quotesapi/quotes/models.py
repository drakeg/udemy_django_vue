from django.db import models

# Create your models here.
class Quote(models.Model):
    quote_author = models.CharField(max_length=50)
    quote_body = models.TextField()
    context = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_author