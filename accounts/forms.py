from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, TutorProfile


class StudentSignUpForm(UserCreationForm):
    major = forms.CharField(max_length=100, required=False)
    year = forms.CharField(max_length=20, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            StudentProfile.objects.create(
                user=user,
                major=self.cleaned_data.get('major', ''),
                year=self.cleaned_data.get('year', '')
            )
        return user


class TutorSignUpForm(UserCreationForm):
    subjects = forms.ChoiceField(
        choices=TutorProfile.SUBJECT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
    )
    rate = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter hourly rate',
            'min': '0',
            'step': '1',
        }),
        label="Hourly Rate ($)",
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False
    )
    location = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city or campus'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            TutorProfile.objects.create(
                user=user,
                subjects=self.cleaned_data.get('subjects', ''),
                rate=self.cleaned_data.get('rate'),
                bio=self.cleaned_data.get('bio', ''),
                location=self.cleaned_data.get('location', ''),
            )
        return user
