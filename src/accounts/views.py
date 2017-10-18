from rest_framework import permissions, routers, viewsets
from django.contrib.auth.models import User, Group
from accounts.serializers import UserSerializer, GroupSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
