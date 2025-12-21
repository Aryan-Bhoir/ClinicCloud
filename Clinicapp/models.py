from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='patient'

class Doctor(models.Model):
    name=models.CharField(max_length=200)
    specialization=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='doctor'



STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
)

class Appointment(models.Model):
    date=models.DateField()
    time=models.TimeField()
    problem=models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table='appointment'