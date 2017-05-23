from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
# Create your views here.

class RegistrationView(SuccessMessageMixin, CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'accounts/registration/registration.html'
    success_url = reverse_lazy('index')
    success_message = "Welcome %(user)s to our website"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict( cleaned_data, user=self.object.username)

class LoginView(SuccessMessageMixin, LoginView):

    template_name = 'accounts/registration/login.html'
    success_message = "%(user)s login successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict( cleaned_data, user=self.request.user)

class LogoutView(RedirectView):
	url = reverse_lazy('accounts:login')
	def get(self, request, *args, **kwargs):
		auth_logout(request)
		messages.add_message(request, messages.INFO, 'Logged out.')
		return super(LogoutView, self).get(request, *args, **kwargs)
"""class LogoutView(SuccessMessageMixin, LogoutView):

    template_name = 'accounts/registration/logout.html'
    success_message = "%(user)s login successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, user=self.request.user)"""