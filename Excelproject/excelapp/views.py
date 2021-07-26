from django.shortcuts import render,HttpResponse
from django.views.generic import View
from rest_framework.status import HTTP_100_CONTINUE, HTTP_201_CREATED
from excelapp.utils.stock_data import stock_data
from django.views.decorators.csrf import csrf_exempt
import sys,os
# Create your views here.


class Home_view(View):
    
    def get(self,request):
        try:
            return render(request,'home.html',context={"title":"Home Page"})
        except:
            return render(request,'home.html',context={"title":"Home Page"})
            # pass
            
class Create_view(View):
    
    @csrf_exempt
    def post(self,request):
        try:
            response=stock_data(request)
            # print("req-==>{}".format(response))
            return HttpResponse(response['message'])
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(str(exc_type) + " " + str(fname) + " " + str(exc_tb.tb_lineno) + " " + str(e))
            return HttpResponse("Some error occured"+e)
