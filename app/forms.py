from django.forms import ModelForm, TimeInput
# from bootstrap4.widgets import BootstrapDateInput, BootstrapTimeInput, BootstrapTextInput
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import *
from django_flatpickr.schemas import FlatpickrOptions

class DeviceOffTimeForm(ModelForm):
    class Meta:
        model = Device
        fields = ['is_off_time']

        widgets = {
            "is_off_time": TimePickerInput(
                options = FlatpickrOptions(time_24hr=True)
            ),
        }

class DeviceOnTimeForm(ModelForm):
    class Meta:
        model = Device
        fields = ['is_on_time']

        widgets = {
            "is_on_time": TimePickerInput(
                options = FlatpickrOptions(time_24hr=True)
            ),
        }