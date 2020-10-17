from django.db import models

# Create your models here.
PERSON_CHOICES=[
    ("Bery","Bery"),
    ("Muema","Muema"),
    ("Jose","Jose")
    ]

class Record(models.Model):
    title=models.CharField(max_length=200)
    person=models.CharField(max_length=100,choices=PERSON_CHOICES)
    pages=models.IntegerField()
    number_of_words=models.IntegerField()
    date=models.DateField(auto_now=True)
    expected_amount = models.IntegerField(null=True, default=0, blank=True)
    amount_received = models.IntegerField(null=True, default=0, blank=True)
    paid=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.date} - {self.title} by {self.person} - {self.pages} pages, {self.number_of_words} words. Payment_Status={self.paid}"
    
