
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ConspectSerializer
from conspect.models import ConspectModel



class GetAllConspectsView(ListAPIView):
    queryset = ConspectModel.objects.prefetch_related('answers').all()
    serializer_class = ConspectSerializer


class DetailConspectView(RetrieveAPIView):
    serializer_class = ConspectSerializer
    queryset = ConspectModel.objects.prefetch_related('answers').all()


@method_decorator(csrf_protect, name='post')
class CreateConspectView(CreateAPIView):
    serializer_class = ConspectSerializer
    queryset = ConspectModel.objects.prefetch_related('answers').all()
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        print(self.request.user, self.request.auth)
        serializer.save(owner=self.request.user)












