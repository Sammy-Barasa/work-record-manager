from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentication.models import User
from fcm_django.models import FCMDevice
from django.urls import reverse
from authentication.utils import Utils
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages


from django.contrib.auth import get_user_model

User = get_user_model()

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

   
    def resend_confirmation_email(self,request,queryset):
        user = User.objects.get_for_model(queryset.model)
        # get user email
        email = user.email
        username = user.username

        # generate token for user
        tokens = user.get_tokens_for_user()
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
        resend_confirmation_email.short_description = 'Resend or send confirmation email'




admin.site.register(User, UserAdmin)

# class FCMDeviceAdmin(admin.ModelAdmin):
#     list_display = ['user', 'registration_id',
#                     'active', 'name', 'type', 'device_id']



# admin.site.register(FCMDevice, FCMDeviceAdmin)
