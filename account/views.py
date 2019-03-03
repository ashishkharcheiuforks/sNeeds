from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework import permissions, generics, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .permissions import AnonPermissionOnly
from .serializers import UserRegisterSerializer, UserSerializer, UserInformationSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class AuthView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"detail": "You are already authenticated"}, status=400)

        data = request.data
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        qs = User.objects.filter(
            Q(username__iexact=username_or_email) |
            Q(email__iexact=username_or_email)
        )
        if qs.exists():
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)

        return Response({"detail": "Invalid credentials!"}, status=401)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonPermissionOnly]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class MyAccountDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_serialize = UserSerializer(request.user)
        return Response(user_serialize.data)

    def put(self, request):
        user = request.user
        user_serialize = UserSerializer(user, request.data)

        try:
            user_information = user.user_information
        except:
            return Response({"This user has no user_information, Please check this first."}, status=400)

        user_information_serializer = UserInformationSerializer(user_information,
                                                                data=request.data)
        # and in if doesn't check both operands if one of them is false
        user_serialize.is_valid()
        user_information_serializer.is_valid()

        if user_information_serializer.is_valid() and user_serialize.is_valid():
            user_serialize.save()
            user_information_serializer.save()
        else:
            return Response({**user_information_serializer.errors, **user_serialize.errors}, status=400)
        return Response({"message": "Success"})
