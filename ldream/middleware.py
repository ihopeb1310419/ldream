# -*- coding: utf-8 -*-
import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

# strip /
EXEMPT_URLS = [re.compile(settings.LOGIN_REDIRECT_URL.lstrip('/'))]

# check in attribute "LOGIN_EXEMPT_URLS" in settings
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	# add url in EXEMPT_URLS
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
class LoginRequireMiddleware:

	# __init__ function
	def __init__(self, get_response):
		self.get_response = get_response

	# __call__ function
	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		# check in attribute "user" in "request"
		assert hasattr(request, 'user')
		# strip / of "path_info"
		path = request.path_info.lstrip('/')

		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
		if path == reverse('accounts:logout').lstrip('/'):
			logout(request)
		elif request.user.is_authenticated() and url_is_exempt and path == reverse('accounts:logout').lstrip('/'):
			logout(request)
		elif request.user.is_authenticated() and url_is_exempt:
			return redirect('/')
		elif request.user.is_authenticated() or url_is_exempt:
			return None
		else:
			return redirect(settings.LOGIN_REDIRECT_URL)