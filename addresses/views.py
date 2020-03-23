from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from addresses.serializers import AddressSerializer
from addresses.models import Address


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.request.user.billingprofile.addresses.all()

    def create(self, request, *args, **kwargs):
        new_address = Address.objects.create(
            billing_profile=request.user.billingprofile,
            address_line_1=request.data.get('address_line_1'),
            address_line_2=request.data.get('address_line_2'),
            city=request.data.get('city'),
            district=request.data.get('district'),
            state=request.data.get('state'),
            postal_code=request.data.get('postal_code')
        )
        return Response({
            'id': new_address.id
        }, status=status.HTTP_200_OK)
