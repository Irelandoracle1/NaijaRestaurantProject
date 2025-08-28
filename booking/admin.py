from django.contrib import admin
from .models import Menu, Booking


# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "time", "guests", "menu", "created_at")
    list_filter = ("date", "time", "menu")
    search_fields = ("user__username", "user__email")
