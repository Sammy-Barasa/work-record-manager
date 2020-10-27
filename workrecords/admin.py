from django.contrib import admin
from workrecords.models import Work, RecordOfWork

# Register your models here.
class WorkRecordAdmin(admin.ModelAdmin):
    list_display = ['date', 'person', 'title', 'pages',
                    'number_of_words', 'expected_amount','cancelled','completed', 'paid', 'amount_received']
    ordering = ['date']
   
admin.site.register(Work,WorkRecordAdmin)
