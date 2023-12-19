from django.contrib.auth import get_user_model

from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

from .serializers import CustomUserCreateSerializer, CustomUserSerializer, ConfirmUserSerializer
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer


class ConfirmUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ConfirmUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(token=request.data['token'])
        if user:
            user[0].is_active = True
            user[0].save()
            return Response({'status': 'Ok'}, status=200)
        return Response({'status': 'Not Found'}, status=404)
