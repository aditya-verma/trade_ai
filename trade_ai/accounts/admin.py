from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    ordering = ('-id',)

    list_display = ('id', 'email', 'is_active')

    search_fields = ['email', 'mobile_no']

    list_filter = ()

    exclude = ('username', 'date_joined')

    readonly_fields = ('activated_at', 'deactivated_at', 'referral_code')

    fieldsets = (
        (None, {
            'fields': (('email', 'mobile_no'),)
        }),
        ('Personal details', {
            'fields': (('first_name', 'date_of_birth'), ('middle_name', 'gender'), 'last_name'),
            'classes': ('wide',)
        }),
        ('Account status', {
            'fields': (
                ('is_active', 'is_staff', 'is_superuser'),
                'activated_at',
                'deactivated_at',
                ('referral_code',),
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
    )


admin.site.disable_action('delete_selected')
