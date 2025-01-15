from django.core.serializers import serialize
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response

class UserListCreateAPIView(generics.ListCreateAPIView):

    def get(self,request):
        users= User.objects.all()
        serilzed_users=UserSerializer(users,many=True)
        return Response(serilzed_users.data)

    def post(self,request):
        serialized=UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)

