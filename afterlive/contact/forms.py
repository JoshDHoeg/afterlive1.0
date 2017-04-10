from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    subject = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Tell us what you think! Is there anything you want us to add, or is there something you think you can help us with? We are looking for porofessional photographers, who want to promote their work. We are also looking for enthusiastic people who want love music and want to relive the best experiences of their lives.'})
    )
