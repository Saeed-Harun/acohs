from django.urls import path
from . import views

urlpatterns = [
    path('my-results/', views.my_results, name='my_results'),
    path('result-pdf/', views.result_pdf, name='result_pdf'),
]
