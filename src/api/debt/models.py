from django.db import models


class AccountsReceivable(models.Model):

    fio = models.CharField("ФИО обучающегося", max_length = 255)
    personal_number = models.CharField("Личный номер", max_length = 20)
    contract_number = models.CharField("Номер договора", max_length = 255)
    accounts_receivable = models.DecimalField("Сумма задолженности", max_digits=10, decimal_places=2)
    status = models.BooleanField("Актуальность", default = True)
    file_created_time = models.DateTimeField("Дата создания файла")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.fio

    class Meta:

        verbose_name = "Задолженность студентов"
        verbose_name_plural = "Задолженность студентов"


