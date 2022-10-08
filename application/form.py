from django import forms
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    start_date = forms.DateField(initial=datetime.date.today, widget=DateInput)
    end_date = forms.DateField(initial=datetime.date.today, widget=DateInput)

