# from django import forms
# from .models import Visite
#
# class VisitForm(forms.ModelForm):
#     class Meta:
#         model = Visite
#         fields = ['title', 'email', 'number', 'subject', 'message']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'number': forms.TextInput(attrs={'class': 'form-control'}),
#             'subject': forms.TextInput(attrs={'class': 'form-control'}),
#             'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
#         }