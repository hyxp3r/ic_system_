from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import validate_student
from .tandem import StudentData


@api_view(["GET"])
def get_students(request, personal_number:str) -> Response:
    student =  StudentData().get(personal_number = personal_number)
    personal_number_serializer = validate_student(student)
    return Response({"student":student[0]})