from rest_framework import serializers
from workrecords.models import Work, RecordOfWork, TypeOfWorkChoices
from django.contrib.auth import get_user_model

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id','user','topic', 'assigned_by', 'category_of_work','order_number','pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid','last_modified']
        read_only_fields = ['id','last_modified']
        depth = 1
        # validate
        def validate(self, attr):
            return attr



class WorkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['user', 'topic', 'assigned_by', 'category_of_work', 'order_number', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid', 'last_modified']
        
        # validate

        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            user_id = validated_data.pop('user')
            assigned_by_id = validated_data.pop('assigned_by')
            category_of_work_id = validated_data.pop('category_of_work')
            work = Work.objects.create(
                user=self.context['request'].user, assigned_by=assigned_by_id, category_of_work=category_of_work_id, **validated_data)
            record = RecordOfWork.objects.create(work=work)
            return work

class UpdateWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id','topic', 'date','category_of_work', 'order_number', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        read_only_fields = ['id', 'topic', 'date']
        
        # validate

        def validate(self, attr):
            return attr


class CategoryOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfWorkChoices
        fields = ['id','work_type']
        read_only_fields = ['id']
        
        # validate

        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            type_of_work = TypeOfWorkChoices.objects.create(user=self.context['request'].user,**validated_data)
            return type_of_work
