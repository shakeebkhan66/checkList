from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserRegisterSerializer
from rest_framework.response import Response


# Create your views here.
class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
