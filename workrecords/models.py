from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#person choices to be personalised


User= get_user_model()
# type choices to be personalised
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
    
class Work(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.CharField(max_length=200)
    person=models.CharField(max_length=100)
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

    def get_choices(self,id):
        CHOICES = ()
        choices= PersonChoises.objects.get(user=get_user_model().objects.get(pk=id))
        for choice in choices:
            CHOICES.append((choice.name,choice.name))
            return CHOICES   
    def __str__(self):
        return f"{self.user} {self.date} - {self.topic},{self.type_of_work} by {self.person} - {self.pages} pages, {self.number_of_words} words. Cancelled_status={self.cancelled} Completed_status={self.completed} Payment_Status={self.paid}"
    
class RecordOfWork(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.work}"

