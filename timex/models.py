from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_id = models.EmailField()
    message = models.TextField()
    def _str_(self):
        return self.first_name
        

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    def _str_(self):
        return self.email_id


    



