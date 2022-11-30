from django.db import models
from django.core.validators import RegexValidator


class VehicleOwnerInformation(models.Model):
    class Meta:
        db_table: str = "VehicleOwnerInformation"

    VOLUNTEER_GROUP = [
        ("Faculty", ""),
        ("Student", "")
    ]

    SCHOOL_NAMES = [
        ("MIT-SOE", "MIT School of Engineering"),
        ("MIT-ID", "MIT Institue of Design"),
        ("MANET", "Maharashtra Academy of Naval Education & Training"),
        ("MIT-SBSR", "MIT School of Bio-Engineering Sciences and Research")
    ]

    REGNO_REGEX = "[MITU].*"

    # owner details
    first_name: models.CharField = models.CharField(
        "first name", max_length=64)
    last_name: models.CharField = models.CharField(
        "middle name", max_length=64)
    email: models.EmailField = models.EmailField(
        "email address", max_length=320)

    # institute affiliation details
    volunteer_type: models.CharField = models.CharField(
        "volunteer type", max_length=7, choices=VOLUNTEER_GROUP)
    registration_number: models.CharField = models.CharField("institute registration number",
                                                             max_length=15,
                                                             validators=[
                                                                 RegexValidator(REGNO_REGEX, message="Invalid Registration Number")],
                                                             primary_key=True)
    college_name: models.CharField = models.CharField(
        "college_name", max_length=255, choices=SCHOOL_NAMES)


class VehicleInformation(models.Model):
    class Meta:
        db_table: str = "VehicleInformation"

    VEHICLE_TYPES = [
        ("MC", "Scooters, Bikes"),
        ("LMV", "Cars"),
        ("TRANS", "Transport Vehicles")
    ]

    LICENSE_PLATE_REGEX = "(([A-Za-z]){2,3}(|-)(?:[0-9]){1,2}(|-)(?:[A-Za-z]){2}(|-)([0-9]){1,4})|(([A-Za-z]){2,3}(|-)([0-9]){1,4})"

    vehicle_type: models.CharField = models.CharField(
        max_length=6, choices=VEHICLE_TYPES)
    vehicle_make: models.CharField = models.CharField(max_length=255)
    license_plate: models.CharField = models.CharField(
        max_length=15, validators=[RegexValidator(LICENSE_PLATE_REGEX, message="Invalid License Plate")])

    registration_number: models.ForeignKey = models.ForeignKey(
        VehicleOwnerInformation, on_delete=models.CASCADE)
