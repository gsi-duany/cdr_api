from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView

class LoginAPI(APIView):
    permission_classes = [AllowAny]

    """
       Login method with "username" and "password"
       ---
       Parameters:
          - name: username
            description: Username to login in system
            required: true
            type: string
          - name: password
            description: Password to login in system
            required: true
            type: string
        return ('token', user}
    """


    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, user: UserSerializer(user).data},
                        status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request, * args, ** kwargs):
    """
        Login method with "username" and "password"
    ---
    parameters:
       - name: username
         description: Foobar long description goes here
         required: true
         type: string
       - name: password
         required: true
         type: string
         return ('token', user}
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, value= Token.objects.get_or_create(user=user)
    user_data = UserSerializer(user).data
    return Response({'token': token.key, 'user': user_data},
                    status=HTTP_200_OK)

