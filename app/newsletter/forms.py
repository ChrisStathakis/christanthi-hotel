from django import forms

from .models import NewsLetter


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsLetterForm(BaseForm, forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'width': '50%'}))
    acceptRules = forms.BooleanField(required=True, label='Αποδέχομαι τους όρους χρήσης')

    class Meta:
        model = NewsLetter
        fields = ['email', 'acceptRules']


class NewsLetterFormEng(BaseForm, forms.ModelForm):
    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'width:50%'}))
    acceptRules = forms.BooleanField(required=True, label='Accept the terms of Use')

    class Meta:
        model = NewsLetter
        fields = ['email', 'acceptRules']
