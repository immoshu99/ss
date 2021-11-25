from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from .models import Donation,Contact,Profile,RequestChange

class RequestChangeForm(forms.ModelForm):

    class Meta:
        model = RequestChange
        fields = '__all__'
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileEditForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['blood','city','thana','phone','name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','blood','city','thana','phone']



class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Password',widget=PasswordInput)

    password2 = forms.CharField(label='Repeat password',widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password did not matched ')
        
        return cd['password2']


class DonationCreateForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ['name','phone','bloodgroup','city','thana','last_donation']



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)