from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .models import Task

# Create your views here.

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    try:
        username = request.data.get('email')
        password = request.data.get('password')
        if username is None or password is None:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if not user:
            return Response(
                {'error': 'Invalid Credentials'},
                status=status.HTTP_404_NOT_FOUND
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response({"error": "somthing went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def new_user(request):
    try:
        user = User(
            username=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        user.save()
        return Response({"status":"done"}, status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response({"error": "somthing went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
