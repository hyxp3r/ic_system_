from datetime import datetime, timezone
import logging
import os

from django.db import IntegrityError, transaction
from celery import shared_task
import pandas as pd

from src.debt.models import AccountsReceivable
from ic_system.settings import FILE_PATH

logger = logging.getLogger("ic_system.api.debt.tasks")


def get_mtime() -> datetime:
    try:
        mtime = os.path.getmtime(FILE_PATH)
    except FileNotFoundError as e:
        logger.error("File doesn't exist:", e)
        raise FileNotFoundError()

    mtime_readable = datetime.fromtimestamp(mtime, tz = timezone.utc)
    return mtime_readable

def get_from_file() -> dict:
    df = pd.read_excel(FILE_PATH, usecols = ["Субконто1.Юридическое физическое лицо.Наименование", 
                                                "Учащийся.Номер личного дела",
                                                "Субконто2.Номер договора",
                                                "Сумма Конечный остаток Дт"
                                                ])
    df["Сумма Конечный остаток Дт"] = df["Сумма Конечный остаток Дт"].fillna(0)
    df = df[df["Сумма Конечный остаток Дт"] != 0]
    data = df.to_dict("records")
    return data

def get_file_time_from_db () -> datetime|None:
    
    record = AccountsReceivable.objects.filter(status = True).first()
    if record:
        file_db_time = record.file_created_time
        return file_db_time
        
    
def insert_with_update(data:dict, mtime_readable:datetime):

    with transaction.atomic():
        try:  
            AccountsReceivable.objects.filter(status = True).update(status = False)
            for item in data:
                accounts = AccountsReceivable(fio = item["Субконто1.Юридическое физическое лицо.Наименование"],
                                            personal_number = item["Учащийся.Номер личного дела"],
                                            contract_number = item["Субконто2.Номер договора"],
                                            accounts_receivable = item["Сумма Конечный остаток Дт"],
                                            file_created_time = mtime_readable)
                accounts.save()
        except IntegrityError as e:
            logger.error(f"Database error: {e}")
            raise IndentationError(e)

def insert(data:dict, mtime_readable:datetime):

    with transaction.atomic():
        try:
            for item in data:   
                accounts = AccountsReceivable(fio = item["Субконто1.Юридическое физическое лицо.Наименование"],
                                            personal_number = item["Учащийся.Номер личного дела"],
                                            contract_number = item["Субконто2.Номер договора"],
                                            accounts_receivable = item["Сумма Конечный остаток Дт"],
                                            file_created_time = mtime_readable)
                accounts.save()    
        except IntegrityError as e:
            logger.error(f"Database error: {e}")
            raise IndentationError(e)           

@shared_task   
def update_debt_table() -> None:
    """Update table 'AccountsReceivable' with debt via file """
    mtime_readable = get_mtime()
    file_db_time = get_file_time_from_db()

    if mtime_readable == file_db_time:
        logger.info("File has not changed")
        return "File has not changed "
    data = get_from_file()
    if not file_db_time:
        logger.info("Table is empty. Started execution.")
        insert(data, mtime_readable)
    else:
        logger.info("Updating and inserting data")
        insert_with_update(data, mtime_readable)
