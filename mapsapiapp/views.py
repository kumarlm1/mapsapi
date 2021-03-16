from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import CreateUserSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from .models import Users

# Create your views here.

class Users_Create_endpoint(APIView):

    def get(self,request):

        u=Users.objects.all()
        create_users=CreateUserSerializer(u,many=True)
        return JsonResponse(create_users.data,status=201,safe=False)

    def post(self,request):
        data=JSONParser().parse(request)
        
        create_users=CreateUserSerializer(data=data)
        if create_users.is_valid():
            create_users.save()
            username=create_users.data['username']
            password=create_users.data['password']
            email=create_users.data['email']
            first_name=create_users.data['first_name']
            last_name=create_users.data['last_name']

            # user = Users.objects.create()
            # user.username=username
            # user.password=password
            # user.email=email
            # user.first_name=first_name
            # user.last_name=last_name
            # user.save()

            user1=User.objects.create_user(username,email,password)
            
            token=Token.objects.create(user=user1)

            return JsonResponse(f"{token}",status=201,safe=False)
        return JsonResponse(create_users.errors,status=400,safe=False) 
def password_reset(request):
    return render(request,'mapsapiapp/passreset.html')


