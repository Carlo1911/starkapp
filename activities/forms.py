from django import forms

class ActivityForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'El campo nombre es requerido'})
    price = forms.CharField(error_messages={'required': 'El campo precio es requerido'})
    end_date = forms.DateTimeField(error_messages={'required': 'El campo fecha fin es requerido'}, input_formats=['%m/%d/%Y %H:%M %p'])
    attendance = forms.IntegerField(error_messages={'required': 'El campo registrados es requerido'})
    start_date = forms.DateTimeField(error_messages={'required': 'El campo fecha inicio es requerido'}, input_formats=['%m/%d/%Y %H:%M %p'])