from django import forms
from django.core.mail import send_mail

class QuoteForm(forms.Form):
    name = forms.CharField(label=       'Full Name           ', max_length=50, required=True)
    email = forms.EmailField(label=     'Email               ', max_length=50, required=True)
    company = forms.CharField(label=    'Company Name        ', required=False)
    description = forms.CharField(label='Project Description ', max_length=1000 , widget=forms.Textarea, required=True)
    deadline = forms.DateField(label=   'Approximate Deadline', required=False )
    def send_email(self):
        #sends an email using data collected with the form

        deadline=str(self.cleaned_data['deadline'])

        send_mail(self.cleaned_data['name']+' from '+self.cleaned_data['company']+" requests a quote",
        #subject
        self.cleaned_data['email']+"""
"""+
        self.cleaned_data['description']+"""
by """+deadline,
        #body

        'noreply@graywebdesigns.com',
        #sending email

        ['graywebdesigns@gmail.com']
        )
        pass
