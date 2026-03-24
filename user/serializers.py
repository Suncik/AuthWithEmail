from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.core.mail import send_mail
import random   


def generate_code():
    return str(random.randint(100000, 999999))

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email', 'username', 'password']
        extra_kwargs={
            'password': {'write_only': True}  
        }  
        
    # def create(self, validated_data):   
    #     user=User.objects.create_user(
    #         email=validated_data['email'],
    #         username=validated_data['username'],
    #         password=validated_data['password']
            
    #     )       
        
    #     EmailVerification.objects.filter(user=user).delete()
    
    #     code = generate_code()

    #     EmailVerification.objects.create(
    #         user=user,
    #         code=code
    #     )
        
    #     send_mail(
    #         subject='Your verification code',
    #         message=f'your code is: {code}',
    #         from_email=None,
    #         recipient_list=[user.email],
            
    #     )
        
    #     return user
    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": username
            }
        )

        if created:
            user.set_password(password)
            user.is_active = False
            user.save()

       
        code = generate_code()
        EmailVerification.objects.create(user=user, code=code)

        send_mail(
             message=f'Your code is: {code}',
            from_email=None,
            recipient_list=[user.email],
            subject='Your verification code',
        )
   

        
#========================================VERIFY=================================
    
class VerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    code=serializers.CharField(max_length=6)
    
    def validate(self, data):
        email=data.get('email')  
        code=data.get('code')    
        
        # try:
        #     user=User.objects.get(email=email)
        # except User.DoesNotExist:
        #     raise serializers.ValidationError('user not found')
        
        # try:
        #     verification=EmailVerification.objects.get(user=user, code=code)
        # except EmailVerification.DoesNotExist:
        #     raise serializers.ValidationError('Invalid code')
        
        

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("User not found")

        # verification = EmailVerification.objects.filter(user=user, code=code).first()
        # if not verification:
        #     raise serializers.ValidationError("Invalid code")
        
        try:
            verification=EmailVerification.objects.filter(user=user, code=code).latest('created_at')
        except EmailVerification.DoesNotExist:
            raise serializers.ValidationError("Invalid code")
        
        if verification.is_expired():
            raise serializers.ValidationError('code expired')
        
        data['user']=user
        data['verification']=verification   
        return data
    def create(self, validated_data):
        user=validated_data['user']   
        verification=validated_data['verification']
        
        user.is_active=True 
        user.is_verified=True  
        user.save()
        
        verification.delete()    
        
        return {"message": "Email verified successfully"}         
    
#=====================================LOGIN=================================

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    
    def validate(self, data): 
        email=data.get('email')  
        password=data.get('password')  
        user=authenticate(username=email, password=password)
        
        if not user:  
            raise serializers.ValidationError('invalid credentials')
        
        if not user.is_active:
            raise serializers.ValidationError('User not verified')
        refresh=RefreshToken.for_user(user)
        
        return{    
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user":{
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "is_verified": user.is_verified
            }
        }
#============================ResendCode================================

class ResendCodeSerialaizer(serializers.Serializer):
    email=serializers.EmailField()
    
    def validate(self, data):
        email=data['email']   
        
        try:  
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        if user.is_verified:    
            if not user.is_active:
                user.is_active=True
                user.save()
                
            raise serializers.ValidationError("User already verified")
        
        data['user']=user    
        return data  
    
    def create(self, validated_data):     
        user=validated_data['user']
        
        EmailVerification.objects.filter(user=user).delete()
        code = generate_code()
        EmailVerification.objects.create(user=user, code=code)
        user.is_active=True
        user.is_verified=True
        user.save()
        send_mail( 
            subject='Your verification code',
            message=f'Your resend code is: {code}',
            from_email=None,
            recipient_list=[user.email],
        )
        return user  
    
    
# =========================FORGOT PASSWORD=================================

class ForgotPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField()
    def validate(self, data):
        user=User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError("user not found")
        
        data['user']=user  
        return data
    def create(self, validated_data):
        user=validated_data['user']
        
        EmailVerification.objects.filter(user=user, type='reset').delete()
        
        code=generate_code()
        EmailVerification.objects.create(
            user=user,
            code=code,
            type='reset'    
        )
        send_mail(
            subject='Password reset code',
            message=f'Your reset code is: {code}',
            from_email=None,
            recipient_list=[user.email],
        )
        
        return user  

       
        
#==============================RESET PASSWORD==========================

class ResetPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField()
    code=serializers.CharField()
    new_password=serializers.CharField()
    
    def validate(self, data):  
        email=data['email']
        code=data['code']
        
        user=User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("user not found")
        
        user=User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError('User not found')
        
        try:
            verification=EmailVerification.objects.filter(
                user=user,
                code=code,
                type='reset'
            ).latest('created_at')
            
        except EmailVerification.DoesNotExist:
            raise serializers.ValidationError("Invalid code")
        
        if verification.is_expired():
            raise serializers.ValidationError("Code Expired")
        
        data["user"]=user
        data["verification"]=verification
        return data
    
    def create(self, validated_data):
        user=validated_data["user"]
        verification=validated_data["verification"]
        
        user.set_password(validated_data["new_password"])
        user.save()
        
        verification.delete()  
        
        return user  


# ===========================POST=======================================

class PostSerializer(serializers.ModelSerializer):    
    class Meta:  
        model=Post
        fields=['id', 'content', 'title', 'created_at']
    
# bunday shaklda yozishimiz ham mumkin 
        
# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
    
    