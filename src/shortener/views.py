from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):   #function based view
    return HttpResponse("HELLO {sc}".format(sc=shortcode))

class KirrCBView(View):   #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        return HttpResponse("HELLO AGAIN {sc}".format(sc=shortcode))

