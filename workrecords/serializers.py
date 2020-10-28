from rest_framework import serializers
from workrecords.models import Work
from django.contrib.auth import get_user_model

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'user', 'topic', 'person', 'type_of_work', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        read_only_fields = ['id']
        extra_kwargs = {'user': {'write_only': True}}
        # validate
        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            work= Work.objects.create(**validated_data)
            return work


class UpdateWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['topic', 'person', 'type_of_work', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        
    

        
