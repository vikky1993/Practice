#from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

from navaform.forms import NavaForm

#def home(request):
#	return render(request, "index.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "templates/index.html", {})

class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "templates/index.html", {})

# class HomeView(SuccessMessageMixin, CreateView):
# 	template_name = 'templates/index.html'
# 	form_class  = NavaForm
# 	success_url = '/'

# 	def get_success_message(self, cleaned_data):
# 		print(cleaned_data)
# 		return "Thank you for contacting us! We will get back to you."
