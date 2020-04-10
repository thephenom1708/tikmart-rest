from rest_framework import permissions, generics, viewsets

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'id'
    serializer_class = TagSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query is not None:
            return Tag.objects.filter(title__icontains=query)
        else:
            return Tag.objects.all()
