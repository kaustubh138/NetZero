from django.urls import path
from .views import SurveyForm

urlpatterns = [
    path('/form', SurveyForm.as_view(), name="Survey"),
]
