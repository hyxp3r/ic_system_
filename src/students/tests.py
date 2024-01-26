from django.test import TestCase
from rest_framework import serializers

from .serializers import validate_student

class ValidateStudentTestCase(TestCase):
    def test_validate_student_with_valid_input(self):
        validate_student('123456')

    def test_validate_student_with_empty_input(self):
        with self.assertRaises(serializers.ValidationError):
            validate_student(None)





