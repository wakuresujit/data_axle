from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import date  # Import the 'date' object from the 'datetime' module


class UpcomingEventsAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        # Implement logic to retrieve upcoming events based on the current date
        return Event.objects.filter(event_date__gte=date.today()).order_by('event_date')

class SendEventEmailAPIView(generics.UpdateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        # Implement logic to retrieve birthday events to be emailed today
        return Event.objects.filter(
            event_date=date.today(),
            sent_status=False,
            event_type__name='Birthday',  # Assuming you have a "Birthday" event type
        )

    def perform_update(self, serializer):
        event = serializer.instance
        # Construct the email content
        subject = "Happy Birthday, {}!".format(event.employee.name)
        context = {'name': event.employee.name, 'event_date': event.event_date}
        html_message = render_to_string('birthday_email_template.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['wakuresujit10@gmail.com']  # Replace with your recipient's email

        # Send the email
        try:
            send_mail(
                subject,
                plain_message,
                from_email,
                recipient_list,
                html_message=html_message,
            )
            # Update the event's sent_status
            event.sent_status = True
            event.save()
        except Exception as e:
            # Handle any email sending errors and update the error_message
            event.error_message = str(e)
            event.save()


from django.template.loader import render_to_string

# Define a dictionary with the data you want to pass to the template
context = {'name': 'Sujit', 'event_date': '2023-09-19'}

# Render the template with the data
html_message = render_to_string('birthday_email_template.html', context)
