from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GuestEmail

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name', 'last_name', 'mobile', 'admin')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'password', 'mobile')}),
        ('Full name', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'first_name' 'last_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']

    class Meta:
        model = GuestEmail


admin.site.register(GuestEmail, GuestEmailAdmin)
