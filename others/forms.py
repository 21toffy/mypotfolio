from django import forms

class ContactForm(forms.Form):


    email = forms.CharField(required=True ,label='email', widget=forms.EmailInput(attrs={'class':'forms-control'}))

    subject = forms.CharField(required=True ,max_length=100, label='subject', widget=forms.TextInput(attrs={'class':'forms-control'}))

    message = forms.CharField(required=True ,label='message', widget=forms.Textarea(attrs={'class':'forms-control'}))
    
    cc_myself = forms.BooleanField(required=False)

