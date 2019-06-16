"""Account app views."""
from django.views.generic import TemplateView

from account.models import User
from django.shortcuts import get_object_or_404


class Base(TemplateView):
    """Base view."""
    template_name = None
    additional_context = None

    def get_context_data(self, **kwargs):
        """Overrde context."""
        context = super().get_context_data(**kwargs)
        context.update({
            "title": 'UserStore',
        })
        if self.additional_context:
            context.update(self.additional_context)
        return context


class UserView(Base):
    """User list view."""
    template_name = 'user_list.html'
    additional_context = {
        "users": User.objects.all(),
    }


class PersonView(UserView):
    """Personal page view."""
    template_name = 'person.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        context = self.get_context_data(user=user, **kwargs)
        return self.render_to_response(context)
