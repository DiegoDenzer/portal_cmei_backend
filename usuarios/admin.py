from django.contrib import admin

# Register your models here.
from usuarios.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email' ,'last_login']
    exclude = ['date_joined', 'is_superuser', 'last_login']
