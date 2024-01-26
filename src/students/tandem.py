import logging

import pyodbc
from pyodbc import Connection , Row, OperationalError
from django.conf import settings

logger = logging.getLogger("ic_system.api.debt.tasks")

class StudentData:
    server = settings.TANDEM_HOST
    database = settings.TANDEM_DB
    username = settings.TANDEM_USERNAME
    password = settings.TANDEM_PASSWORD

    def connect(self):
        try:
            self.conn:Connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+
                                            self.server+
                                            ';DATABASE='+
                                            self.database+
                                            ';UID='+
                                            self.username+
                                            ';PWD='+self.password, timeout=2)
        except OperationalError as e:
            logger.error(f"Tandem server is not available:", exc_info=True)
            raise e
       
    def get(self, personal_number:str) -> Row | None:  
        self.connect()
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
            f"""
            SELECT DISTINCT
            VPO.BOOKNUMBER booknumber
            FROM vpo2_view  VPO
            WHERE VPO.STATUSTITLE = 'активный' 
            and VPO.BOOKNUMBER = '{personal_number}'
           
            """)
            row = cursor.fetchone()
            return row