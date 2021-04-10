from django.contrib import admin
from workrecords.models import Work, RecordOfWork, PersonChoises, TypeOfWorkChoices

# Register your models here.
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'order_number','date','created_by','assigned_by','assigned_to', 'category_of_work','pages',
                    'number_of_words', 'expected_amount', 'cancelled', 'completed', 'paid', 'amount_received', 'user', 'last_modified', 'date_paid']
    ordering = ['last_modified']


class RecordOfWorkAdmin(admin.ModelAdmin):
    list_display = ['work']


class PersonChoisesAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


class TypeOfWorkChoicesAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_type']

admin.site.register(Work,WorkAdmin)
admin.site.register(RecordOfWork,RecordOfWorkAdmin)
admin.site.register(PersonChoises, PersonChoisesAdmin)
admin.site.register(TypeOfWorkChoices, TypeOfWorkChoicesAdmin)
