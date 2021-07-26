from django.urls import path,re_path
from . import views

app_name="stocks"

urlpatterns = [
    path("",views.Home_view.as_view(),name="create_stock"),
    path("create",views.Create_view.as_view(),name="save_stock"),
]
