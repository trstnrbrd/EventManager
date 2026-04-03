from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(attrs={'class': 'form-control'}),
            'cus_name':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Juan dela Cruz'}),
            'cus_ph':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 09171234567'}),
            'name':         forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'cus_name':     'Customer Name',
            'cus_ph':       'Phone Number',
            'name':         'Event',
            'booking_date': 'Booking Date',
        }
