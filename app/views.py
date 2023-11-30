from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
from .serializers import DeviceSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def devices(request):
    devices = Device.objects.all()
    content = {'devices': devices}
    return render(request, 'app/devices.html', content)

def updateDeviceState(request, pk):
    device = Device.objects.get(id=pk)
    state = device.state
    device.state = not state
    device.save()
    return redirect("devices")


def updateDeviceOffTime(request, pk):
    device = Device.objects.get(id=pk)
    form = DeviceOffTimeForm(instance = device)
    if request.method == 'POST':
        form = DeviceOffTimeForm(request.POST, instance = device)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'app/time_form.html', context)


def updateDeviceOnTime(request, pk):
    device = Device.objects.get(id=pk)
    form = DeviceOnTimeForm(instance = device)
    if request.method == 'POST':
        form = DeviceOnTimeForm(request.POST, instance = device)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'app/time_form.html', context)


@api_view(['GET', 'POST'])
def deviceList(request):
    if request.method == "GET":
        try:
            queryset = Device.objects.all()
            serializer = DeviceSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            imei = str(request.data.get('imei')).strip()
            imei_check = Device.objects.filter(imei=imei)
            if not imei.isdigit():
                raise Exception("imei sanlardan ıbarat bolıwı kerek")
            if len(imei) != 16:
                raise Exception('imei 16 cifr bolıwı kerek')
            if imei_check.exists():
                raise Exception("Bul imei paydalanılǵan, basqa imei kiritiń")
            serializer = DeviceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Qátelik, qayta kiritiń"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE",'PATCH'])
def deviceDetail(request, imei):
    try:
        device = Device.objects.get(imei=imei)
    except Device.DoesNotExist:
        return Response({"message": "Maǵlumat tabılmadı"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DeviceSerializer(device, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = DeviceSerializer(instance=device, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        device.delete()
        return Response({"message": "Maǵlumat óshirildi"}, status=status.HTTP_204_NO_CONTENT)
