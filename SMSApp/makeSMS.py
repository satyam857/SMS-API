from SMSApp import sms
from django.http import HttpResponse
from django import forms

class FormName(forms.Form):
    phone = forms.NumberInput()
    message = forms.Textarea()
    username = forms.CharField()
    password = forms.CharField()
