from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(label='Your message', max_length=255)