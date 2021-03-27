from rest_framework import serializers
from workrecords.models import PersonChoises
from django.contrib.auth import get_user_model


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonChoises
        fields = ['id','name', 'email', 'phone']
        read_only_fields = ['id']
        
        # validate

        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            person = PersonChoises.objects.create(
                user=self.context['request'].user, **validated_data)
            return person


class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonChoises
        fields = ['id', 'name', 'email', 'phone']
        read_only_fields = ['id']

        # validate

        def validate(self, attr):
            return attr

        # create
        def update(self, instance,validated_data):
            instance.name = validated_data.get('name')
            instance.email = validated_data.get('email')
            instance.phone = validated_data.get('phone')
            return instance
