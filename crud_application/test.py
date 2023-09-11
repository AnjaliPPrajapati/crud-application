from django.urls import reverse
import json
import unittest
from crud_application.models import Student
from rest_framework.test import APITestCase
from crud_application.views import common_test_func

class TestCrudApp(APITestCase):
    def test_api_add_student(self):
        self.request_object = {
            'first_name':"Anjali",
            'last_name':"Prajapati"
        }
        common_test_func(self, self.request_object,'add-student', 'Record inserted successfully')

        
        
