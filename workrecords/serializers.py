from rest_framework import serializers
from workrecords.models import Work
from django.contrib.auth import get_user_model

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'topic', 'person', 'type_of_work', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'cancelled', 'completed', 'amount_received', 'paid']
        read_only_fields = ['id']
        # create
        # validate
        # update
        def validate(self, attr):
            return attr

        def create(self, validated_data):
            user_id=self.kwargs['user_id']
            user=get_user_model().objects.get(pk=user_id)
            if user is not None:
                return Work.objects.create(user=user,**validated_data)
            return {"messge":"you are not a registered user, please register"}