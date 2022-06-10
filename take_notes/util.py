from email.errors import HeaderMissingRequiredValue
from django import forms

class InputURL(forms.Form):
    heading = forms.CharField(max_length=255)
    description = forms.TextInput()
