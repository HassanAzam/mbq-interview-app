from django.contrib.auth.models import BaseUserManager
from interview_app.utils import constants
from interview_app.users import models

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError('Users must have a valid e-mail address')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
            name=kwargs.get('name')
        )

        user.set_password(password)
        user.save()

        return user

    
    def create_interviewer(self, email, password=None, **kwargs):

        user = self.create_user(email, password, kwargs)

        user.user_type = constants.ID_USER_TYPE_INTERVIEWER
        user.save()

        return user
    

    def create_interviewee(self, email, password=None, **kwargs):
        """
        superuser(admin)
        """

        user = self.create_user(email, password, kwargs)

        user.user_type = constants.ID_USER_TYPE_INTERVIEWEE
        user.save()

        return user


    def create_superuser(self, email, password=None, **kwargs):
        """
        superuser(admin)
        """

        print(email)
        print(password)
        print(kwargs)
        user = self.create_user(email, password, kwargs)

        user.user_type = constants.ID_USER_TYPE_ADMIN
        user.is_admin = True
        user.save()

        return user
