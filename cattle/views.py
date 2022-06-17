from rest_framework import generics
from .serializer import CattleSerializer
from .models import Cattle
from .permissions import IsOwnerOrReadOnly

class CattleList(generics.ListCreateAPIView):
    queryset = Cattle.objects.all()
    serializer_class = CattleSerializer


class CattleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,) # adds permissions
    queryset = Cattle.objects.all()
    serializer_class = CattleSerializer