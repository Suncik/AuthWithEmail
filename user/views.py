from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, VerifySerializer, ResendCodeSerialaizer, \
    LoginSerializer


#======================REGISTER=============================

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer    


#===========================VERIFY=======================================

class VerifyView(generics.CreateAPIView):
    serializer_class=VerifySerializer  
    
#===========================RESEND CODE====================================

class ResendCodeView(generics.CreateAPIView):  
    serializer_class=ResendCodeSerialaizer  
    


#=============================LOGIN==========================================

class LoginView(APIView):   
      @swagger_auto_schema(request_body=LoginSerializer)
      def post(self, request):
        seriializer=LoginSerializer(data=request.data)
        seriializer.is_valid(raise_exception=True)
        
        return Response(seriializer.validated_data, status=status.HTTP_200_OK)
        
    
