from django.shortcuts import render, redirect
from ..forms import VehicleInfoForm


def form(request):
    form = VehicleInfoForm()
    return render(request, 'form.html', {'form': form})
