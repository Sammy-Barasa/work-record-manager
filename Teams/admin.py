from django.contrib import admin
from Teams.models import Team,TeamMembership
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'team_name', 'owned_by', 'date_created']
    ordering = ['date_created']


class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'writer',
                    'date_joined', 'is_request_accepted']
    ordering = ['date_joined']


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMembership, TeamMembershipAdmin)
