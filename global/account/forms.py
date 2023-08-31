from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import ContactMessage

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']

from contact.models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['class'] = 'form-control custom-class-for-name'
        self.fields['email'].widget.attrs['class'] = 'form-control custom-class-for-email'
        self.fields['message'].widget.attrs['class'] = 'form-control custom-class-for-message'

