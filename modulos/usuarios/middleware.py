from __future__ import unicode_literals
import threading
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model
from django.utils.functional import lazy
from django.conf import settings

class CurrentuserMiddleware(MiddlewareMixin):
    """
    Always have access to the current user
    """
    __users = {}

    def process_request(self, request):
        """
        Store user info
        """
        self.__class__.set_user(request.user)

    def process_response(self, request, response):
        """
        Delete user info
        """
        self.__class__.del_user()
        return response

    def process_exception(self, request, exception):
        """
        Delete user info
        """
        self.__class__.del_user()

    @classmethod
    def get_user(cls, default=None):
        """
        Retrieve user info
        """
        return cls.__users.get(threading.current_thread(), default)

    @classmethod
    def set_user(cls, user):
        """
        Store user info
        """
        if isinstance(user, str):
            User = lazy(get_user_model, settings.AUTH_USER_MODEL)
            user = User.objects.get(username=user)
        cls.__users[threading.current_thread()] = user

    @classmethod
    def del_user(cls):
        """
        Delete user info
        """
        cls.__users.pop(threading.current_thread(), None)

    