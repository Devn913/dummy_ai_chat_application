from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password , check_password
from .models import User , Chat
import secrets
import time 

class Register(APIView):

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username, password=make_password(password) , tokens=4000)
        
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
    
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                token = secrets.token_hex(16)
                user.token = token
                user.save()
                return Response({'message': 'Login successful', 'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUEST)
        
        
    
class ChatView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try: 
            user = User.objects.get(token=token)
            message = request.data.get('message')\
            
            if not message:
                return Response({'error': 'Invalid message'}, status=status.HTTP_400_BAD_REQUEST)
            
            if user.tokens < 100:
                return Response({'error': 'Insufficient tokens'}, status=status.HTTP_400_BAD_REQUEST)
            
            user.tokens -= 100
            user.save()

            message_reponse = 'Response to ' + message
            timestamp = time.time()

            Chat.objects.create(user=user, message=message, response=message_reponse , timestamp=timestamp)

            return Response({
                'message': message,
                'response': message_reponse
            }, status=status.HTTP_201_CREATED)
            
        except User.DoesNotExist:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        
    
    
    
    
class TokenBalance(APIView):
    def get(self , request):
        print(request.headers)
        token = request.headers.get('Authorization')
        print(token)
        if not token:
            return Response({'error': 'Unauthorized Token Not Found'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            user = User.objects.get(token=token)
            return Response({'tokens': user.tokens}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        

    
