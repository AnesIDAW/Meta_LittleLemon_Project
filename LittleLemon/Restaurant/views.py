from django.shortcuts import render
from .forms import BookingForm
from .models import Menu, Booking
from django.core import serializers
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def message(request):
    return Response({"message": "This view is protected"})
    




def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def reservations(request):
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)
    # return render(request, "bookings.html", {"bookings": booking_json})
    bookings_data = {"bookings": bookings}
    return render(request, "bookings.html", {"bookings": bookings_data})

def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}

    return render(request, "menu.html", main_data)


def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else: 
        menu_item = ""

    return render(request, "menu_item.html", {"menu_item": menu_item})


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", bookings)

    return HttpResponse(booking_json, content_type="application/json")