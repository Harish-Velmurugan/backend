from homepage.models import User_Professional,User_Personal,bids
from rest_framework import viewsets,permissions
from .serializers import user_professional_serializer,user_personal_serializer,bids_serializer

class UserProfessionalViewSet(viewsets.ModelViewSet):

    queryset = User_Professional.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = user_professional_serializer

class UserPersonalViewSet(viewsets.ModelViewSet):

    queryset = User_Personal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = user_personal_serializer

class BidsViewSet(viewsets.ModelViewSet):

    queryset = bids.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = bids_serializer