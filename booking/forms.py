# booking/forms.py
from django import forms
from django.db import IntegrityError
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "guests", "menu"]

    def save(self, commit=True):
        """
        Catch DB uniqueness collisions and surface a nice form error
        instead of a 500 error.
        """
        try:
            return super().save(commit=commit)
        except IntegrityError:
            self.add_error(None, "Sorry, that date and time are already booked.")
            