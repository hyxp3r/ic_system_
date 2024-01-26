
from django.contrib import admin
from django.urls import path

from src.debt.views import get_debts
from src.students.views import get_students


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/debts/<str:personal_number>', get_debts),

    path('api/v1/students/<str:personal_number>', get_students),
]