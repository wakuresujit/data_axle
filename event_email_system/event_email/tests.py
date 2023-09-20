from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Event, EventType, Employee
from datetime import date





class BirthdayEmailTestCase(TestCase):

    def setUp(self):
        # Set up test data (e.g., create employees and birthday events)
        self.client = APIClient()
        self.employee_sujit = Employee.objects.create(name='Sujit', email='sujit@example.com', hire_date='2023-01-15')
        self.birthday_event = EventType.objects.create(name='Birthday',
                                                       template='event_email/birthday_email_template.html')
        self.birthday = Event.objects.create(employee=self.employee_sujit, event_type=self.birthday_event,
                                             event_date='2023-09-19')



    def test_birthday_email_sending(self):
        url = reverse('send-event-email', kwargs={'pk': self.birthday.id})
        response = self.client.put(url, format='json')

        # Debugging: Print the response content
        print(response.content)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.birthday.refresh_from_db()
        self.assertTrue(self.birthday.sent_status)





