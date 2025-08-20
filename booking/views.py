# booking/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Booking, Menu
from .forms import BookingForm


class HomeView(TemplateView):
    template_name = "booking/home.html"

class MenuListView(TemplateView):
    template_name = "booking/menu_list.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["menu_items"] = Menu.objects.all()
        return ctx

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/booking_list.html"
    context_object_name = "bookings"
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by("date", "time")

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class BookingUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking_list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            return self.form_invalid(form)

class BookingDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking_list")
