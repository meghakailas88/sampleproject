from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NewUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .permissions import UpdateOwnProfile


class NewUserViewSet(viewsets.ModelViewSet):
    """API to view user(s)"""
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAuthenticated, UpdateOwnProfile]


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserLogoutView(APIView):
    """delete auth token when user log out"""

    def get(self, request):
        request.user.auth_token.delete()
        return Response({"code": 200, "message": "ok"})





