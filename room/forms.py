from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(label='Your message', max_length=255, widget=forms.TextInput(attrs={"id" : "message-input"}))