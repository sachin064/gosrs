
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from .serializers import Userserializer

from .models import Users
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from clasifiedpro.settings import MEDIA_ROOT


@api_view(['POST','GET'])
def register_view(request):
        if request.method == 'POST':
            try:
                email = request.data.get('email')
                user = Users.objects.get(email=email)
                photo_path = str(user.photo.file)
                firstname = user.firstname
                lastname = user.lastname
                context = {
                    "first_name": firstname,
                    "last_name": lastname,
                    "photo": photo_path
                }
                if user is not None:
                    return Response({'exist':context, 'message':'user already exists'})
            except Exception as e:
                first_name = request.data.get('first_name')
                user_name = request.data.get('user_name')
                last_name = request.data.get('last_name')
                password = request.data.get('password')
                photo = request.data.get('photo')
                context = {
                    "firstname": first_name,
                    "lastname": last_name,
                    "username":user_name,
                    "email": email,
                    "password": password,
                    "photo": photo,
                }
                r = Users(**context)
                r.save()
                return Response({"message": "Registered sucesfully"})
        else:
            return Response({"status":"fail","message":"pagenot found"})


class UserDetail(APIView):
    def get_object(self, id):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, id):
        try:
            Users = self.get_object(id)
            serializer = Userserializer(Users)
            return Response(serializer.data)
        except Exception as e:
            return Response({'status':'Fail', 'statuscode':'400', 'message':'user not found'})

    def delete(self, request, id):
        try:
            users = self.get_object(id)
            users.delete()
            return Response({'status':'success','statuscode':'204','messsage':'useredeleted successfully'})
        except Exception as e:
            return Response({'status':'fail','statuscode':'400','messsage':'user not found'})

    def put(self, request, id,):
        update = self.get_object(id)
        serializer = Userserializer(update, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'success','statuscode':'204','message':'Data updatefailed'})
        except Exception as e:
            return Response({'status':'success','statuscode':'204','message':'invalid data'})


@api_view(['GET','POST'])
def login_view(request):
    try:
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')
            r = Users.objects.get(email=email)
            if r.password == password:
                return Response({"messsage":"login sucesfully"})
            else:
                return Response({"message":"invalid password"})
    except Exception as e:
        return Response({"message":" wrong email id or entered the reqired fields"})


@api_view(['GET','POST'])
def postman(request):
    if request.method == 'GET':
        return Response({"message":"hii helllo"})