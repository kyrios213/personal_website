from django import forms

class SendEmailForm(forms.Form):
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=255)