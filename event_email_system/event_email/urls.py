from django.urls import path
from . import views

urlpatterns = [
    path('upcoming-events/', views.UpcomingEventsAPIView.as_view(), name='upcoming-events'),
    path('send-event-email/<int:pk>/', views.SendEventEmailAPIView.as_view(), name='send-event-email'),
]
