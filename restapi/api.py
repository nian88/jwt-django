from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated  # <-- Here

class MemberViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('name', )
    pagination_class = None
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        qs = super(MemberViewSet, self).get_queryset(*args, **kwargs)
        qs = qs.filter(id=self.request.user.id)
        return qs
