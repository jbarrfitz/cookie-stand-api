from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer


class CookieStandList(ListCreateAPIView):
    def get_queryset(self):
        queryset = CookieStand.objects.filter(owner_id=self.request.user.id)
        return queryset

    serializer_class = CookieStandSerializer


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = CookieStand.objects.filter(owner_id=self.request.user.id)
        return queryset

    serializer_class = CookieStandSerializer
