from django.forms import ModelForm
from django import forms

class create_form(forms.Form):
    search_string = forms.CharField(max_length=2048, label='', 
                                    widget=forms.TextInput(
                                        attrs={
                                            'placeholder': 'Search Images',
                                            'id': "email-header02-0",
                                            'class': "form-control display-7",
                                            'style': 'border: 1px solid #F9C74F;',
                                        }
    ))

