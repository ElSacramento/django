from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):

	list_display = ('username', 'nickname', 'email', 'id')
	fieldsets = ((None, {'fields': ('nickname', 'email', 'password', 'avatar')}),)

    # def admin_avatar(self, instance):
    #     return instance.avatar and u'<img src="{0}" width="100px" />'.format(
    #         instance.avatar.url
    #     )
    # admin_avatar.allow_tags = True
    # admin_avatar.short_description = u'Avatar'

admin.site.register(User, UserAdmin)