from rest_framework import generics, permissions, status
from rest_framework.response import Response

from lucky_draw.models import LuckyDraw, LuckyDrawProfile
from lucky_draw.serializers import LuckyDrawSerializer, LuckyDrawProfileSerializer


class LuckyDrawAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LuckyDrawSerializer

    def get_object(self):
        lucky_draw_obj = LuckyDraw.objects.filter(active=True).first()
        return lucky_draw_obj


class LuckyDrawProfileAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LuckyDrawProfileSerializer

    def get_queryset(self):
        return self.request.user.lucky_draw_profiles.all()

    def get_object(self):
        return self.get_queryset().get(lucky_draw__id=self.kwargs['lucky_draw_id'])

    def update(self, request, *args, **kwargs):
        lucky_draw_profile = self.get_object()
        lucky_draw_profile.participated = True
        lucky_draw_profile.save()
        return Response({
            'success': True
        }, status=status.HTTP_200_OK)
