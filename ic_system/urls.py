
from django.contrib import admin
from django.urls import path

from src.debt.views import get_debts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/debts/<str:personal_number>', get_debts),
]