from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccountsReceivable
from .serializers import DebtSerializer, PersonalNumber

@api_view(["GET"])
def get_debts(request, personal_number:int) -> Response:
    personal_number_serializer = PersonalNumber(data = {"personal_number":personal_number})
    valid = personal_number_serializer.is_valid(raise_exception=True)
    my_model =  get_object_or_404(AccountsReceivable, personal_number=personal_number)
    serializer = DebtSerializer(my_model)
    return Response(serializer.data)