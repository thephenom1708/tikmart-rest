from .signals import object_viewed_signal


class ObjectViewedMixin(object):
    def get_context_data(self, *args, **kwargs):
        request = self.request
        if request.user.is_authenticated:
            context = super(ObjectViewedMixin, self).get_context_data(*args, **kwargs)
            instance  = context.get('object')
            if instance:
                object_viewed_signal.send(instance.__class__, instance=instance, request=request)
            return context