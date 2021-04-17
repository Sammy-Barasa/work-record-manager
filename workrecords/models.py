from django.db import models
from django.contrib.auth import get_user_model
from phone_field import PhoneField
from Teams.models import Team

# Create your models here.
#person choices to be personalised


User= get_user_model()

# type choices to be personalised
class PersonChoises(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email= models.EmailField(default="person@example.com", max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    def __str__(self):
        return f"{self.name}--({self.user})"
    
class TypeOfWorkChoices(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.work_type}"
    
class Work(models.Model):
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="given_to")
    topic=models.CharField(max_length=200)
    assigned_by = models.ForeignKey(PersonChoises, on_delete=models.CASCADE,null=True, blank=True)
    is_from_team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True,blank=True)
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
    date_paid = models.DateTimeField(blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    
    
 
    def __str__(self):
        return f"{self.created_by} {self.date} - {self.topic},{self.category_of_work} by {self.assigned_by} - {self.pages} pages, {self.number_of_words} words. Cancelled_status={self.cancelled} Completed_status={self.completed} Payment_Status={self.paid}"
    


