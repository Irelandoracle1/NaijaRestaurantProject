from django import forms
from django.db import IntegrityError
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "guests", "menu"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",   # HTML5 date picker
                }
            ),
            "time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",   # HTML5 time picker
                }
            ),
            "guests": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
            "menu": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def save(self, commit=True):
        """
        Catch DB uniqueness collisions and surface a nice form error
        instead of a 500 error.
        """
        try:
            return super().save(commit=commit)
        except IntegrityError:
            self.add_error(
                None,
                "Sorry, that date and time are already booked."
            )
