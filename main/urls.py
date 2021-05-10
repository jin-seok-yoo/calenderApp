from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="main"),
    path('viewSeat', views.viewSeat, name="seat"),
    path('checkSeat', views.checkSeat, name="checkSeat"),
    # path('save/', views.saveData, name="saveData"),
]
