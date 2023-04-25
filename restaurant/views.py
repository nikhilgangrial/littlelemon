from django.core import exceptions
from django.shortcuts import render
from rest_framework import permissions, response, status, generics

from .forms import BookingForm
from .models import Booking
from .models import Menu
from .serializers import BookingSerializer, MenuSerializer


# Create your views here.
class Home(generics.ListAPIView):
    def get(self, request, **kwargs):
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'index.html')
        else:
            return response.Response("Bad Request", status.HTTP_400_BAD_REQUEST)


class About(generics.ListAPIView):
    def get(self, request, **kwargs):
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'about.html')
        else:
            return response.Response("Bad Request", status.HTTP_400_BAD_REQUEST)


class Reservations(generics.ListAPIView):
    def get(self, request, **kwargs):
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'bookings.html')
        elif request.user:
            request.GET.get('date')
            if request.user.is_superuser:
                bookings_ = Booking.objects.all()
            else:
                bookings_ = Booking.objects.filter(first_name=request.user.username).all()

            return response.Response(BookingSerializer(bookings_, many=True).data)


class Login(generics.ListAPIView):
    def get(self, request, **kwargs):
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'login.html')
        return response.Response("Bad Request", status.HTTP_400_BAD_REQUEST)


class Book(generics.ListCreateAPIView):
    def get(self, request, **kwargs):
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            form = BookingForm()
            context = {'form': form}
            return render(request, 'book.html', context)
        return response.Response("Bad Request", status.HTTP_400_BAD_REQUEST)


# Add your code here to create new views
class MenuView(generics.ListAPIView):
    def get(self, request, **kwargs):
        menu_data = Menu.objects.all()
        main_data = {"menu": menu_data}
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'menu.html', {"menu": main_data})
        else:
            return response.Response(MenuSerializer(menu_data, many=True).data, status.HTTP_200_OK)


class DisplayMenuItem(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        if kwargs["pk"]:
            try:
                menu_item = Menu.objects.get(pk=kwargs["pk"])
            except exceptions.ObjectDoesNotExist:
                menu_item = ""
        else:
            menu_item = ""
        if 'text/html' in request.META.get('HTTP_ACCEPT'):
            return render(request, 'menu_item.html', {"menu_item": menu_item})
        else:
            if menu_item:
                return response.Response(MenuSerializer(menu_item).data, status.HTTP_200_OK)
            else:
                return response.Response({"message": "Not Found"}, status.HTTP_404_NOT_FOUND)


class BookingView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        data = request.data

        try:
            exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
                reservation_slot=data['reservation_slot']).exists()
        except KeyError:
            exist = 2
        if not exist:
            booking = Booking(
                first_name=request.user.username,
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
            return response.Response(BookingSerializer(booking).data, status.HTTP_201_CREATED)
        if exist == 2:
            return response.Response("Bad Parameters", status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response("Already Exists", status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.all().filter(reservation_date=date)
            return response.Response(BookingSerializer(bookings, many=True).data, status.HTTP_200_OK)
        return response.Response("Bad Request", status.HTTP_400_BAD_REQUEST)
