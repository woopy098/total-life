import requests
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Clinician, Patient, Appointment
from .serializers import ClinicianSerializer, PatientSerializer, AppointmentSerializer

class ClinicianViewSet(viewsets.ModelViewSet):
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        npi_number = request.data.get("npi_number")
        first_name = request.data.get("first_name")
        last_name =  request.data.get("last_name")
        state = request.data.get("state")
        response = requests.get(f"https://npiregistry.cms.hhs.gov/api/?number={npi_number}&first_name={first_name}&last_name={last_name}&state={state}&version=2.1")

        if response.status_code == 200:
            data = response.json()
            if data["result_count"] == 0:
                return Response({"error": "Invalid Details"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
