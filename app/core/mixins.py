from app.accounts.models import User

class CreatorUpdaterMixin(object):

    def create(self, request, *args, **kwargs):
        if 'created_by' not in request.data:
            user = User.objects.first()
            request.data['created_by'] = user.id

        return super(CreatorUpdaterMixin, self).create(request, args, kwargs)