from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from EmotionTalk.auth_app.models import Profile

UserModel = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('id', 'username', 'is_staff',)
    list_filter = ('id', 'username', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Permissions', {'fields': ('is_staff', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('username',)
    ordering = ('id',)


admin.site.register(UserModel, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('email', 'image', 'first_name', 'last_name', 'user', 'last_emotions',)
    list_display = ('user_id', 'email', 'first_name', 'last_name',)
    list_filter = ('user_id', 'email', 'first_name', 'last_name',)

