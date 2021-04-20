from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User
from fcm_django.models import FCMDevice
from django.urls import reverse
from authentication.utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_staff',
                    'is_verified', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
            }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    actions = ['resend_confirmation_email']

    @admin.action(description='Resend or send confirmation email')
    def resend_confirmation_email(self,request,queryset):
        # get user email
        email = queryset.email
        username = queryset.username

        # generate token for user
        tokens = queryset.get_tokens_for_user()
        accesstoken = tokens["access"]

        # chain email to email_veify endpoint
        endpoint = reverse('verify_endpoint')
        # current site domain
        domain = get_current_site(request).domain
        print(domain)
        # constract link from http/https + domain + verify_endpoint and q=access
        verifylink = 'https://'+domain+endpoint+'?token=' + str(accesstoken)
        print(verifylink)
        # constract the message
        subject = "Verify your Email"

        # create message
        body = "Hi, "+username + \
            ",WorkRecordManager wants to verify your email.use this link to do so.\n" + verifylink
        data = {'subject': subject, 'body': body,
                'to_email': email}

        # send email
        Utils.send_email(data=data)




admin.site.register(User, UserAdmin)

# class FCMDeviceAdmin(admin.ModelAdmin):
#     list_display = ['user', 'registration_id',
#                     'active', 'name', 'type', 'device_id']



# admin.site.register(FCMDevice, FCMDeviceAdmin)
