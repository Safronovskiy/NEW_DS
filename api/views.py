from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ConspectSerializer
from conspect.models import ConspectModel



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

