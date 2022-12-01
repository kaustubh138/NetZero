from typing import List, Dict

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpRequest
from rest_framework.response import Response


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
