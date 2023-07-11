from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    start_date = forms.DateField(initial=datetime.date.today, widget=DateInput, label="A partir du ")
    end_date = forms.DateField(initial=datetime.date.today, widget=DateInput, label="Jusqu'au ")


class ImageForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today, widget=DateInput, label="Date ")
