from django.shortcuts import render

# Create your views here.
from citasapi.models import *
from citasapi.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class DoctorList(APIView):
    """
    List all doctors, or create a new doctor.
    """
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        serializer = DoctorListSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Specialtyid = serializer.data["id"]
            mSpecialty = Doctor.objects.get(pk=Specialtyid)
            mSpecialty.department = serializer.data["department"]
            mSpecialty.name = serializer.data["name"]
            mSpecialty.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class ClientList(APIView):
    """
    List all doctors, or create a new doctor.
    """
    def get(self, request, format=None):
        doctors = Client.objects.all()
        serializer = ClientListSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        serializer = ClientListSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Specialtyid = serializer.data["idClient"]
            mSpecialty = Client.objects.get(pk=Specialtyid)
            mSpecialty.password = serializer.data["password"]
            mSpecialty.email = serializer.data["email"]
            mSpecialty.age = serializer.data["age"]
            mSpecialty.name = serializer.data["name"]
            mSpecialty.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class SpecialtyList(APIView):
    """
    List all doctors, or create a new doctor.
    """
    def get(self, request, format=None):
        doctors = Specialty.objects.all()
        serializer = SpecialtyListSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, format=None):
        serializer = SpecialtyListSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Specialtyid = serializer.data["id"]
            mSpecialty = Specialty.objects.get(pk=Specialtyid)
            mSpecialty.description = serializer.data["description"]
            mSpecialty.name = serializer.data["name"]
            mSpecialty.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SpecialtyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
