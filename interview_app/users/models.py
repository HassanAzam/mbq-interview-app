from django.contrib.auth.models import AbstractBaseUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from interview_app.utils import constants
from django.db import models
from interview_app.users.manager import UserManager
from django.contrib.auth.models import PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    """Default user for Interview Web Application."""

    USER_TYPE_CHOICES = (
        (constants.ID_USER_TYPE_ADMIN, constants.USER_TYPE_ADMIN),
        (constants.ID_USER_TYPE_INTERVIEWER, constants.USER_TYPE_INTERVIEWER),
        (constants.ID_USER_TYPE_INTERVIEWEE, constants.USER_TYPE_INTERVIEWEE)
    )

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Reference to user role
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


