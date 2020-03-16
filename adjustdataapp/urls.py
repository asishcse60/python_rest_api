from django.urls import path
from adjustdataapp.views import DataSetListFilter
app_name = 'dataSearch'
urlpatterns = [
    path('dataSearch/', DataSetListFilter.as_view(), name='data')
]