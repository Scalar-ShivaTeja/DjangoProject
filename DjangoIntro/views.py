from django.core.serializers import serialize
from django.http import HttpRequest,HttpResponse
from django.shortcuts import get_object_or_404

from DjangoIntro.models import User

import json


def Users(request:HttpRequest) -> HttpResponse :
    if request.method == "GET":
        user_list=User.objects.all()
        # user_list = User.objects.filter(is_deleted=False)

        user_name_list=[f'id=>{user.id}, name=>{user.name}' for user in user_list]
        serialized_users=json.dumps(user_name_list)

        # first_user=user_list[0]
        # serailized_user=json.dumps(first_user)
        return HttpResponse(serialized_users)
    elif request.method == "POST":
        body=json.loads(request.body);
        user=User(name=body['name'],email=body['email'])
        user.save()
        return  HttpResponse(json.dumps({'id':user.id,'name':user.name}))

def get_upfate_delete_user(request:HttpRequest,id:int)->HttpResponse:
    user = User.objects.get(id=id)
    # user=get_object_or_404(User,id=id)

    if request.method == "GET":
        return HttpResponse(json.dumps({'id':user.id,'name':user.name,'email':user.email,'address':user.address}))
    elif request.method == "PUT":
        body=json.loads(request.body);
        user.name=body['name']
        user.email=body['email']
        user.address=body['address']
        user.save()
        return HttpResponse(f'User details updated =>{json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'address': user.address})}')

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(f'Delteted use with')

