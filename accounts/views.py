from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/registration/registration.html'
    success_url = reverse_lazy('index')
    success_message = "Welcome %(user)s to our website"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict( cleaned_data, user=self.object.username)
