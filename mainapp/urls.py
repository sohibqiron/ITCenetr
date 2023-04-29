from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('m-table/',views.mentortable,name='mentor'),
    path('test/',views.testpage,name='test'),
]
