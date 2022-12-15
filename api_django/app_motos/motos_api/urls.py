from django.urls import path
from .views import MotoListaApiView, MotoDetailApiView

urlpatterns = [
    path('', MotoListaApiView.as_view(), name="Moto_list"),
    path('<int:moto_id>/', MotoDetailApiView.as_view(), name="Moto_detail"),
]
