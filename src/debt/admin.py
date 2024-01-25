from django.contrib import admin

from .models import AccountsReceivable

@admin.register(AccountsReceivable)
class AccountsReceivableAdmin(admin.ModelAdmin):
    pass

