from django import forms
from django.core.validators import RegexValidator
from .choices import SCHOOL_NAMES, REGNO_REGEX, VEHICLE_TYPES, LICENSE_PLATE_REGEX


class OwnerPersonalInfo(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=320)


class OwnerInstituteInfo(forms.Form):
    college_name = forms.ChoiceField(choices=SCHOOL_NAMES)
    registration_number = forms.CharField(max_length=15, validators=[
                                          RegexValidator(REGNO_REGEX, message="Invalid Registration Number")])


class VehicleInfo(forms.Form):
    type = forms.ChoiceField(choices=VEHICLE_TYPES)
    license_plate = forms.CharField(
        max_length=15, validators=[RegexValidator(LICENSE_PLATE_REGEX, message="Invalid License Plate Number")])
