from django.forms import forms, ModelForm
from properties.models import Visite


class VisitForm(ModelForm):
    class Meta:
        model = Visite
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError('Please enter a valid email')
        else:
            return email

