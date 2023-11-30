from django.urls import path
from . import views


urlpatterns = [
    path('', views.devices, name='devices'),
    path('device-list/', views.deviceList),
    path('device-detail/<str:imei>/', views.deviceDetail),
    path('update_device_state/<str:pk>/', views.updateDeviceState, name='update_device_state'),
    path('update_device_off_time/<str:pk>/', views.updateDeviceOffTime, name='update_device_off_time'),
    path('update_device_on_time/<str:pk>/', views.updateDeviceOnTime, name='update_device_on_time'),

]