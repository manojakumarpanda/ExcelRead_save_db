import pandas as pd
import os,sys

from excelapp.models import Stock
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import numpy as np
from django.conf import settings
base_dir=getattr(settings,"BASE_DIR")

def stock_data(request):
    try:
        # path = ("G:\Assignment.xlsx ")
        # df = pd.read_excel,engine= 'openpyxl'(path)
        # path=os.path.join(base_dir,"/supporting_docs/Assignment.xlsx")
        df = pd.read_excel(str(base_dir)+"/supporting_docs/Assignment.xlsx")
        df.rename(columns={" ExitPrice":"ExitPrice"},inplace=True)
        df.replace(np.NAN, 0, inplace=True)
        data = df.to_dict('records')
        for obj in data:
            stocks, created = Stock.objects.get_or_create(**obj)
            # print(obj)
            stocks.save()
        return {"message":"Data saved successfully","status":status.HTTP_201_CREATED}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " " + str(e))
        return {"message":"Some error occured","status":status.HTTP_400_BAD_REQUEST}
        








