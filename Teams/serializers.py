from rest_framework import serializers
from Teams.models import Team, TeamMembership
from workrecords.models import Work
from django.contrib.auth import get_user_model


User = get_user_model() 

# Create a team, serialize creating a team

class CreateTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model= Team
        fields = ['owned_by', 'team_name', 'logo']
        def validate(self,attr):
            return attr

        def create(self,validated_data):
            team_name = validated_data.pop('team_name')
            team = Team(team_name=team_name)
            return 

# Team create work, serialize creating work by team manager
class CreateTeamWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work
        fields = ['assigned_to', 'is_from_team', 'category_of_work']

# Team add member, serialize adding a  memeber to the team
class AddTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields =['team','writer']

# Team get members, serialize members information to minial
class GetTeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone','mpesa_no']

# Team get work records, serialize work records that belong to the team
class GetTeamWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'topic', 'category_of_work', 'order_number', 'pages', 'number_of_words',
                  'date', 'expected_amount', 'is_from_team', 'cancelled', 'completed', 'amount_received', 'paid', 'last_modified', 'date_paid']

# Team search for memebers, serialize members information to id and email for search purposes
class GetMembersForSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
