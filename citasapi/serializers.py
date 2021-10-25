from django.contrib.auth.models import  Group
from .models import *
from rest_framework import serializers
class ReservationSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Reservation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
     class Meta:
        model = Message
        fields = '__all__'

class DoctorListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    messages = MessageSerializer(many=True,read_only=True)
    reservations = ReservationSerializer(many=True,read_only=True)
    class Meta:
        model = Doctor
        fields = ('id','name','department','year','specialty','description','messages','reservations')
class ClientListSerializer(serializers.ModelSerializer):
    idClient = serializers.IntegerField()
    messages = MessageSerializer(many=True,read_only=True)
    reservations = ReservationSerializer(many=True,read_only=True)
    class Meta:
        model = Client
        fields = ('idClient','name','email','age','password','messages','reservations')
class SpecialtyListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    doctors = DoctorListSerializer(many=True,read_only=True)
    class Meta:
        model = Specialty
        fields = ('id','name','description','doctors')
        read_only_fields = ["doctors"]
class SpecialtyMiniSerializer(serializers.ModelSerializer):
      class Meta:
        model = Specialty
        fields = ['id']
class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtyMiniSerializer(read_only = True)
    messages = MessageSerializer(many=True,read_only=True)
    reservations = ReservationSerializer(many=True,read_only=True)
    class Meta:
        model = Doctor
        fields = ('id','name','department','year','specialty','description','messages','reservations')
    def create(self, validated_data):
        
        doctor = Doctor(**validated_data)
        specialty = Specialty.objects.get(pk = 1)
        doctor.specialty = specialty
        doctor.save()
        return doctor
class ClientSerializer(serializers.ModelSerializer):
    
    messages = MessageSerializer(many=True,read_only=True)
    reservations = ReservationSerializer(many=True,read_only=True)
    class Meta:
        model = Client
        fields = ('idClient','name','email','age','password','messages','reservations')
class SpecialtySerializer(serializers.ModelSerializer):
    
    doctors = DoctorListSerializer(many=True,read_only=True)
    class Meta:
        model = Specialty
        fields = ('id','name','description','doctors')
        read_only_fields = ["doctors"]


