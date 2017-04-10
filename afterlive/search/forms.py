from django import forms

class SubscribeForm(forms.Form):

    Sub_Name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    Sub_Email = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    
