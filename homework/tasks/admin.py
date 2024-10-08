from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from django.http import HttpRequest
from django.http.response import HttpResponse
from .models import UserProfile
from .forms import CustomUserCreationForm

# Inline to show UserProfile fields in the admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fields = ('grade', 'section')

# Override UserAdmin to include the inline and custom form
class CustomUserAdmin(BaseUserAdmin):
    # add_form = CustomUserCreationForm  # Use the custom form

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(CustomUserAdmin, self).add_view( *args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(CustomUserAdmin, self).change_view( *args, **kwargs)

    # # This is needed so that custom fields are available when creating a user
    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return []
    #     return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# admin.site.register(UserProfile)
