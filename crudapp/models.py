from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Page(models.Model):

    # user=models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True) # for protected like if user has creted the page then you can not delete that user
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True}) # by limit_choice only staff can make the page
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name=models.CharField(max_length=70)
    page_cat=models.CharField(max_length=70)
    page_publish_date=models.DateField()



