from django.db import models

class Clinician(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    state= models.CharField(max_length=2)
    npi_number= models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Patient (models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    date_of_birth= models.DateField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Appointment(models.Model):
    status_choice=[('pending','Pending'),('completed','Completed'),('cancelled','Cancelled')]

    patient= models.ForeignKey(Patient,on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician,on_delete=models.CASCADE)
    appointment_time= models.TimeField()
    status= models.CharField(max_length=10, choices=status_choice, default='pending')


    def __str__(self):
        return f"{self.patient}-{self.appointment_time}({self.status})"
 