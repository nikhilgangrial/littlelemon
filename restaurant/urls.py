from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),                    # notAPI
    path('about/', views.About.as_view(), name="about"),            # notAPI
    path('book/', views.Book.as_view(), name="book"),               # notAPI
    path('login/', views.Login.as_view(), name="login_browser"),    # notAPI
    path('reservations/', views.Reservations.as_view(), name="reservations"),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu/<int:pk>/', views.DisplayMenuItem.as_view(), name="menu_item"),
    path('booking/', views.BookingView.as_view(), name='bookings'),
]
