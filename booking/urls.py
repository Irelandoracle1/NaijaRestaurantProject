# reservations/urls.py
from django.urls import path
from .views import (
    HomeView, MenuListView,
    BookingListView, BookingCreateView, BookingUpdateView, BookingDeleteView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("menu/", MenuListView.as_view(), name="menu"),

    path("bookings/", BookingListView.as_view(), name="booking_list"),
    path("bookings/new/", BookingCreateView.as_view(), name="booking_create"),
    path("bookings/<int:pk>/edit/", BookingUpdateView.as_view(), name="booking_update"),
    path("bookings/<int:pk>/delete/", BookingDeleteView.as_view(), name="booking_delete"),
]