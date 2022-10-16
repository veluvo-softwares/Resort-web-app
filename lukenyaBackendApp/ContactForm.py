from django import forms
from django.core import validators

from .models import contact


class ContactForm(forms.ModelForm):
    Name = forms.CharField(max_length=100, widget=forms.TextInput, validators=[validators.MinLengthValidator(3)])
    Email = forms.EmailField(max_length=254, widget=forms.EmailInput)
    Subject = forms.CharField(max_length=500)
    Message = forms.CharField(max_length=2000, widget=forms.Textarea)

    def clean_Name(self):
        Name = self.cleaned_data['Name']
        if len(Name) < 3:
            raise forms.ValidationError("Name can not be less than 3 characters")
        return Name

    def clean_Email(self):
        Email = self.cleaned_data['Email']
        return Email

    def clean_Subject(self):
        Subject = self.cleaned_data['Subject']
        return Subject

    def clean_Message(self):
        Message = self.cleaned_data['Message']
        return Message

    class Meta:
        model = contact
        fields = ('Name', 'Email', 'Subject', 'Message')

        # or fields = "__all__"