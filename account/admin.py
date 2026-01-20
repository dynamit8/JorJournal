from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'get_is_staff', 'get_is_active')
    list_filter = ('user__is_staff','user__is_active','user__date_joined')
    search_fields = ('user__username','user__email')

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'
    get_username.short_description = 'Username'

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

    def get_is_staff(self, obj):
        return obj.user.is_staff
    get_is_staff.admin_order_field = 'user__is_staff'
    get_is_staff.boolean = True
    get_is_staff.short_description = 'Is Staff'

    def get_is_active(self, obj):
        return obj.user.is_active
    get_is_active.admin_order_field = 'user__is_active'
    get_is_active.boolean = True
    get_is_active.short_description = 'Is Active'

    def get_date_joined(self, obj):
        return obj.user.date_joined
    get_date_joined.admin_order_field = 'user__date_joined'
    get_date_joined.short_description = 'Date Joined'
