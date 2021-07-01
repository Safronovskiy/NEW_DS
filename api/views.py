from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import ConspectSerializer
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





# ------------------OLD VERSION----------------

@api_view(['GET', 'POST'])
def save_conspect(request):
    if request.method == 'POST':
        serializer = ConspectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    queryset = ConspectModel.objects.all()
    serializer = ConspectSerializer(queryset, many=True)
    return Response(serializer.data, status=200)









