from django.contrib.auth import authenticate, login
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts_app.models import CustomUserModel
from .serializers import ConspectSerializer, LoginSerializer
from conspect.models import ConspectModel



class GetAllConspectsView(ListAPIView):
    queryset = ConspectModel.objects.prefetch_related('answers').all()
    serializer_class = ConspectSerializer


class DetailConspectView(RetrieveAPIView):
    serializer_class = ConspectSerializer
    queryset = ConspectModel.objects.prefetch_related('answers').all()


class CreateConspectView(CreateAPIView):
    serializer_class = ConspectSerializer
    queryset = ConspectModel.objects.prefetch_related('answers').all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(self.request.user, self.request.auth)
        serializer.save(owner=self.request.user)


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(request, username = serializer.validated_data.get('username'),
                                         password = serializer.validated_data.get('password'))
            login(request, user)
            return Response(status=200)
        else:
            return Response(status=400)

    # def get(self, request):
    #     queryset = CustomUserModel.objects.all()
    #     serializer = LoginSerializer(queryset, many=True)
    #     return Response(serializer.data)











