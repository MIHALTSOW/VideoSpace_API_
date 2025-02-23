from django.contrib import admin

from Authorization_token.models import AuthorizationUserOnToken


class AuthorizationUserOnTokenAdmin(admin.ModelAdmin):
    exclude = ('groups', 'user_permissions')


admin.site.register(AuthorizationUserOnToken, AuthorizationUserOnTokenAdmin)

