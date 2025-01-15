from django.core.serializers import serialize
from django.http import HttpRequest,HttpResponse

from DjangoIntro.models import User

import json


def Users(request:HttpRequest) -> HttpResponse :
    if request.method == "GET":
        user_list=User.objects.all()

        user_name_list=[user.name for user in user_list]
        serialized_users=json.dumps(user_name_list)

        # first_user=user_list[0]
        # serailized_user=json.dumps(first_user)
        return HttpResponse(serialized_users)
    elif request.method == "POST":
        body=json.loads(request.body);
        user=User(name=body['name'],email=body['email'])
        user.save()
        return  HttpResponse(json.dumps({'id':user.id,'name':user.name}))
