from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone



# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):   # 👈 fixed
        return f"{self.name} — {self.price}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name="bookings")
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["date", "time"], name="unique_booking_slot")
        ]
        ordering = ["-date", "-time"]

    def clean(self):
        dt = timezone.make_aware(
            timezone.datetime.combine(self.date, self.time),
            timezone.get_current_timezone()
        )
        if dt < timezone.now():
            raise ValidationError("You cannot book a past date/time.")

    def __str__(self):   # 👈 fixed
        return f"{self.user} @ {self.date} {self.time} ({self.guests})"
