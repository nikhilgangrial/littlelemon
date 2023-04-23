from django.forms import ModelForm
from django import forms
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    FIELDNAME = forms.FloatField(, required=False)    
    class Meta:
        model = Booking
        fields = "__all__"
