from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
#person choices to be personalised


User= get_user_model()

# type choices to be personalised
class PersonChoises(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email= models.EmailField(default="person@example.com", max_length=254)
    phone= models.IntegerField(default="0700500600")

    def __str__(self):
        return f"{self.name}--({self.user})"
    
class TypeOfWorkChoices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.work_type}"
    
class Work(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic=models.CharField(max_length=200)
    assigned_by = models.ForeignKey(PersonChoises, on_delete=models.CASCADE)
    category_of_work = models.ForeignKey(
        TypeOfWorkChoices, on_delete=models.CASCADE)
    pages=models.IntegerField(default=0)
    number_of_words=models.IntegerField()
    date=models.DateField(auto_now_add=True,editable=False)
    expected_amount = models.IntegerField(null=True, default=0, blank=True)
    cancelled=models.BooleanField(default=False)
    completed = models.BooleanField(default=True)
    amount_received = models.IntegerField(null=True, default=0, blank=True)
    paid=models.BooleanField(default=False)
    order_number = models.CharField(default="#00000",max_length=200)
    last_modified = models.DateTimeField(auto_now=True)
    
 
    def __str__(self):
        return f"{self.user} {self.date} - {self.topic},{self.type_of_work} by {self.person} - {self.pages} pages, {self.number_of_words} words. Cancelled_status={self.cancelled} Completed_status={self.completed} Payment_Status={self.paid}"
    
class RecordOfWork(models.Model):
    work=models.ForeignKey(Work,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.work}"

