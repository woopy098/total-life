from rest_framework import serializers
from .models import Clinician,Appointment,Patient

class ClinicianSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clinician
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields = "__all__"

class AppointmentSerializer (serializers.ModelSerializer):
    # for the JSON to be more readable 
    patient_name= serializers.ReadOnlyField(source='patient.first_name',read_only=True)
    patient_last_name= serializers.ReadOnlyField(source='patient.last_name',read_only=True)
    class Meta:
        model= Appointment
        fields = "__all__"