from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Grade, Section

class CustomUserCreationForm(UserCreationForm):
    grade = forms.ChoiceField(required=True, choices=Grade.choices())
    section = forms.ChoiceField(required=True, choices=Section.choices())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.is_valid():
            print(self.errors)
        if commit:
            user.save()
            # Create or update the UserProfile with the additional fields
            UserProfile.objects.create(
                user=user,
                grade=self.cleaned_data['grade'],
                section=self.cleaned_data['section'],
            )
        return user