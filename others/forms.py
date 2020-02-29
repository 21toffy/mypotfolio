from django import forms

class ContactForm(forms.Form):


    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class':'forms-control'}))

    subject = forms.CharField(label='subject', widget=forms.TextInput(attrs={'class':'forms-control'}))

    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'class':'forms-control'}))
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
