from django.urls import path
from .views  import *
urlpatterns = [     
    
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/',  VerifyView.as_view(), name='verify'  ),
    path('login/', LoginView.as_view(), name='login'), 
    path('resend-code/', ResendCodeView.as_view(), name='resendcode'),
        
]   
