from django import forms
from django.core.validators import RegexValidator
from .choices import SCHOOL_NAMES, REGNO_REGEX, VEHICLE_TYPES, LICENSE_PLATE_REGEX
from .models import VehicleInformation


class VehicleInfoForm(forms.ModelForm):
    class Meta:
        model = VehicleInformation
        fields = "__all__"
