from typing import List, Dict

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.response import Response

from formtools.wizard.views import SessionWizardView
from .forms import OwnerPersonalInfo, OwnerInstituteInfo, VehicleInfo


class Endpoints(APIView):
    """
    Lists all the api endpoints for this application 
    """

    def get(self, request: HttpRequest) -> Response:
        return Response(self.__getEndpoints())

    def __getEndpoints(self) -> List[Dict[str, str]]:
        routes = [
            {
                'Endpoint': '/submit/',
                'method': 'POST',
                'body': None,
                'description': 'submit the form data'
            }
        ]
        return routes


def Home(request):
    return render(request, 'base.html')


class SurveyForm(SessionWizardView):
    form_list = [OwnerPersonalInfo, OwnerInstituteInfo, VehicleInfo]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'multistepform.html', {'data': form_data})
