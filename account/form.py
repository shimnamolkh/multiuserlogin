from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Doctor,Patient

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    address=forms.CharField(required=True)
    city=forms.CharField(required=True)
    state=forms.CharField(required=True)
    pin=forms.FloatField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.email=self.cleaned_data.get('email')
        doctor.address=self.cleaned_data.get('address')
        doctor.profile_photo = self.cleaned_data.get('profile_photo')
        doctor.save()
        return user

class PatientSignUpForm(UserCreationForm):
    
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    address=forms.CharField(required=True)
    city=forms.CharField(required=True)
    state=forms.CharField(required=True)
    pin=forms.IntegerField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient= Patient.objects.create(user=user)
        patient.email=self.cleaned_data.get('email')
        patient.address=self.cleaned_data.get('address')
        patient.profile_photo = self.cleaned_data.get('profile_photo')
        patient.save()
        return user