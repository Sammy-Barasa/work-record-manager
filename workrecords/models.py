from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#person choices to be personalised
PERSON_CHOICES=[
    ("Bery","Bery"),
    ("Muema","Muema"),
    ("Jose","Jose")
    ]

User= get_user_model()
# type choices to be personalised
class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    person=models.CharField(max_length=100,choices=PERSON_CHOICES)
    type_of_work =models.CharField(default="Writing",
        max_length=100)
    pages=models.IntegerField(default=0)
    number_of_words=models.IntegerField()
    date=models.DateField(auto_now=True)
    expected_amount = models.IntegerField(null=True, default=0, blank=True)
    cancelled=models.BooleanField(default=False)
    completed = models.BooleanField(default=True)
    amount_received = models.IntegerField(null=True, default=0, blank=True)
    paid=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} {self.date} - {self.title},{self.type_of_work} by {self.person} - {self.pages} pages, {self.number_of_words} words. Cancelled_status={self.cancelled} Completed_status={self.completed} Payment_Status={self.paid}"
    
class RecordOfWork(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.work}"
class PersonChoises(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}-{self.name}"
class TypeOfWorkChoices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}-{self.work_type}"
