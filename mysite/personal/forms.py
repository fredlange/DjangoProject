from django import forms

class ContactForm(forms.Form):
    """
    Contact form on the contact page
    """
    contact_name = forms.CharField(required = True)
    contact_email = forms.EmailField(required = True)
    content = forms.CharField(required = True, widget=forms.Textarea)
