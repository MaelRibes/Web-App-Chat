from django import forms

class MessageForm(forms.Form):
    text = forms.CharField(label='Your message', max_length=255)