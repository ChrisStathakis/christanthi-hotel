from django import forms

from .models import Contact

CATEGORY_TYPES_ENG = (
        ('a', 'General question'),
        ('b', 'Booking Info'),
    )


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'title', 'name', 'phone', 'text']


class ContactFormEng(BaseForm, forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['email', 'title',  'phone', 'text']
        labels = {
            'title': 'Title',
            'phone': 'Phone',
            'text': 'Message',
            'name': 'Name'
        }


