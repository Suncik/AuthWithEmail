from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Post


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
    
# ==============================Forgot Password=======================================

class ForgotPasswordView(APIView):
    @swagger_auto_schema(request_body=ForgotPasswordSerializer)
    def post(self, request):
        serializer=ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"message": "reset code sent"},
            status=status.HTTP_200_OK
        )  
            
    
    
#===============================Reset Password ========================================

class ResetPasswordView(APIView):
    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request):
        serializer=ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        serializer.save()  
        return Response(  
            {'message': 'reset password successfully'},
            status=status.HTTP_200_OK  
        )
        
#=========================POST==================================

class PostListCreateView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]  
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    
        
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    
      
    
    
        
    
