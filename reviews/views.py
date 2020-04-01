from rest_framework import viewsets, permissions
from reviews.serializers import PostReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostReviewSerializer

    def get_queryset(self):
        return self.request.user.reviews.all()
