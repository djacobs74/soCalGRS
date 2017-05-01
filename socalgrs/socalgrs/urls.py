from django.conf.urls import url
from django.contrib import admin
from website.views import *
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='socalgrs'),
    url(r'^welcome/', WelcomeView.as_view()),
    url(r'^gardenRailways/', GardenRailwaysView.as_view()),
    # url(r'^gardenRailways/(?P<id>[\w\._-]+)/$', GardenRailwaysDetailView.as_view()),
    url(r'^directory/', DirectoryView.as_view()),
    url(r'^contact/', ContactView.as_view()),
    url(r'^membership/', MembershipView.as_view()),
    url(r'^events/', EventsView.as_view()),
    url(r'^newsletters/', NewslettersView.as_view()),
]

if settings.DEBUG: # local path to media
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)