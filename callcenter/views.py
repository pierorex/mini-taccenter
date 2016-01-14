from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView, status
from rest_framework.response import Response
import random
from callcenter.serializers import UserSerializer


class LoginView(APIView):
    
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        print "log in attempt: " + request.data.get('username') + ' ' + \
              request.data.get('password')
        user = authenticate(username=request.data.get('username'),
                            password=request.data.get('password'))
        if user is not None and user.is_active:
            login(request, user)
            return Response(UserSerializer(user).data, status.HTTP_200_OK)
        else:
            return Response({'error': 'Incorrect username/password.'},
                            status.HTTP_400_BAD_REQUEST)
        return Response(data={}, status=status.HTTP_200_OK)
