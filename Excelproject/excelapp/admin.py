from django.contrib import admin
from excelapp.models import Stock

class Stockadmin(admin.ModelAdmin):
    list_display = ['id','Symbol','EntryPrice','ExitPrice','Performance','VolumeChange','InNifty50']


admin.site.register(Stock,Stockadmin)