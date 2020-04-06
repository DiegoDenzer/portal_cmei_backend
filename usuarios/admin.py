from allauth.account.forms import UserForm
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from usuarios.models import MyUser


class CustomUserAdmin(UserAdmin):
    # form = BaseModelFormrForm
    list_display = ['username', 'email', 'last_login']
    # prepopulated_fields = {'username': ('first_name', 'last_name',)}
    # readonly_fields = ['password']

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(MyUser, CustomUserAdmin)