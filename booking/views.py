# booking/views.py
from django.shortcuts import render
from django.http import HttpResponse

def booking_list(request):
    return HttpResponse("Booking List Page")
