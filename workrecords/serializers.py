from rest_framework import serializers
from workrecords.models import Work, RecordOfWork
from django.contrib.auth import get_user_model

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'user', 'topic', 'person', 'type_of_work','order_number','pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        read_only_fields = ['id']
        extra_kwargs = {'user': {'write_only': True}}
        # validate
        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            user_id= validated_data.pop('user')
            work= Work.objects.create(user=context.request.user,**validated_data)
            record = RecordOfWork.objects.create(work=work)
            return work


class UpdateWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'topic', 'person', 'type_of_work', 'order_number', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        read_only_fields = ['id','topic','date','person']
        # validate

        def validate(self, attr):
            return attr
