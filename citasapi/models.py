from django.db import models

class Specialty(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, default=0)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, default=0, max_length=55)
    year = models.IntegerField(blank=True)
    department = models.CharField(default=False, max_length=55)
    specialty = models.ForeignKey(Specialty,on_delete=models.CASCADE, related_name='doctors')
    def __str__(self):
        return self.name

class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    age = models.IntegerField(blank=True)
    password = models.CharField(blank=True, max_length=55)
    def __str__(self):
        return self.nombre

class Reservation(models.Model):
    idReservation = models.AutoField(primary_key=True)
    startDate = models.DateField(blank=True)
    devolutionDate = models.DateField(blank=True)
    score = models.IntegerField(blank=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="rdoctors")
    client =models.ForeignKey(Client,on_delete=models.CASCADE,related_name="rclients")
    def __str__(self):
        return self.nombre

class Message(models.Model):
    idMessage = models.AutoField(primary_key=True)
    messageText = models.CharField(blank=True, max_length=255)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name="mdoctors")
    client =models.ForeignKey(Client,on_delete=models.CASCADE,related_name="mclients")
    def __str__(self):
        return str(self.idMessage)

