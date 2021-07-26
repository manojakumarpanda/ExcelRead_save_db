from django.db import models

class Stock(models.Model):
    id=models.AutoField(primary_key=True)
    Symbol=models.CharField(max_length=200,blank=True,null=True)
    EntryPrice=models.FloatField(null=True,blank=True)
    ExitPrice=models.FloatField(null=False,blank=True)
    Performance=models.FloatField(null=True,blank=True)
    VolumeChange=models.FloatField(null=True,blank=True)
    InNifty50=models.BooleanField(blank=True,null=True)
    
    class Meta:
        db_table="Stocks"
        verbose_name='Stock'
        verbose_name_plural='Stock'
        ordering=['Symbol']






