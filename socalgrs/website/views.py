from django.shortcuts import render
from django import http
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import RequestContext, Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DetailView, TemplateView
from website.models import *

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

class GardenRailwaysView(View):

    def get(self, request):
        railway_query = Railway.objects.filter(category__in=['garden', 'public', 'archive'])

        page_data={
            'railways':railway_query,
        }
        template_name = 'gardenRailways.html'
        return render(request,template_name, page_data)

class GardenRailwaysDetailView(View):  ### view raiway pics page

    def get(self, request):

        single_railway = Railway.objects.get(id=self.kwargs['id'])

        railway_images = RailwayImage.objets.filter(railway=single_railway)
        page_data={
            'railway':single_railway,
            'images':railway_images
        }
        template_name = 'gardenRailwaysDetail.html'
        return render(request,template_name, page_data)
class DirectoryView(View):

    def get(self, request):
        page_data={}
        template_name = 'directory.html'
        return render(request,template_name, page_data)

class ContactView(View):

    def get(self, request):
        page_data={}
        template_name = 'contact.html'
        return render(request,template_name, page_data)

class MembershipView(View):

    def get(self, request):
        page_data={}
        template_name = 'membership.html'
        return render(request,template_name, page_data)

class EventsView(View):

    def get(self, request):
        page_data={}
        template_name = 'events.html'
        return render(request,template_name, page_data)

class NewslettersView(View):

    def get(self, request):
        page_data={}
        template_name = 'newsletters.html'
        return render(request,template_name, page_data)




