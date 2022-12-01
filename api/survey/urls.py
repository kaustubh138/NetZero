from django.urls import path
from .views.form_view import form

urlpatterns = [
    path('survey/form', form),
    #path('', Endpoints.as_view(), name="endpoints"),
]
