from django import forms

class ShareForm(forms.Form):
    file = forms.FileField()
