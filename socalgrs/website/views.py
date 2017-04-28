from django.shortcuts import render
from django import http
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DetailView, TemplateView

class HomeView(View):

    def get(self, request):
        page_data={}
        template_name = 'index.html'
        return render(request,template_name, page_data)

class WelcomeView(View):

    def get(self, request):
        page_data={}
        template_name = 'welcome.html'
        return render(request,template_name, page_data)
