from django import forms

class EmailForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(widget=forms.EmailInput)