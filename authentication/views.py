from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
class createUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()