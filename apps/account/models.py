from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Extended manager for User model."""

    use_in_migrations = False


class UserQuerySet(models.QuerySet):
    """Extended queryset for User model."""


class User(AbstractUser):
    """Base user model."""

    patronymic = models.CharField(_('Patronymic'), max_length=30, blank=True)
    objects = UserManager.from_queryset(UserQuerySet)()

    class Meta:
        """Meta class."""
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        """String method."""
        return "%s:%s" % (self.email, self.get_short_name())

    def get_short_name(self):
        """Get user's short name."""
        short_name = None
        if self.last_name:
            short_name = self.last_name
        if self.patronymic and short_name:
            short_name = '%s %s.' % (short_name, self.patronymic[:1])
        if self.first_name and short_name:
            short_name = '%s %s.' % (short_name, self.first_name[:1])
        return short_name or self.get_full_name()

    def get_full_name(self):
        """Get user's full name.

        Return the first_name plus the patronymic and the last_name,
        with a space in between.
        """
        full_name = '%s %s %s' % (self.first_name, self.patronymic, self.last_name)
        return full_name.strip()