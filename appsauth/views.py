from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Apiresponser import ApiResponser

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
 # user = get_object_or_404(User,username=request.data['username'])
 # return False
 user = User.objects.filter(username=request.data['username']).first()
 # return user
 if not user:
  return ApiResponser.failedResponse("Username atau password salah", status.HTTP_401_UNAUTHORIZED,'error')
 if not user.check_password(request.data['password']):
  return Response({"detail":"Username tidak ditemukan"}, status=status.HTTP_404_NOT_FOUND)
 try:
  Token.objects.get(user=user).delete()
 except:
  False

 token, created = Token.objects.get_or_create(user=user)
 serializer = UserSerializer(instance=user)
 return Response({"token": token.key,"user":serializer.data})


@api_view(['POST'])
def signup(request):
 errors_={}

 if is_valid_email(request.data['email']) == False:
  errors_['email'] = 'Email tidak valid'
 if len(request.data['username'])< 10:
  errors_['username'] = 'Username harus lebih dari 10 character'
 
 if errors_:
  return Response({"error": errors_}, status=status.HTTP_400_BAD_REQUEST)
 
 serializer = UserSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
  user=User.objects.get(username=request.data['username'])
  user.set_password(request.data['password'])
  user.save()
  token = Token.objects.create(user=user)
  return Response({"token":token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
 return Response({"token for {}".format(request.user.email) })


def is_valid_email(email):
 validator = EmailValidator()
 try:
  validator(email)
  return True
 except ValidationError:
  return False