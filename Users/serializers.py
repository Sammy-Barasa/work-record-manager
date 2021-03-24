from rest_framework import serializers
from workrecords.models import PersonChoises
from django.contrib.auth import get_user_model


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonChoises
        fields = ['id', 'user', 'name', 'email', 'phone']
        read_only_fields = ['id']
        extra_kwargs = {'user': {'write_only': True}}
        depth = 2
        # validate

        def validate(self, attr):
            return attr

        # create
        def create(self, validated_data):
            user_id = validated_data.pop('user')
            person = PersonChoises.objects.create(
                user=self.context['request'].user, **validated_data)
            return person
