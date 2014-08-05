from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages


def home(request):
    context = {}
    return render_to_response("core/index.html", context, context_instance=RequestContext(request))


def about(request):
    context = {}
    return render_to_response("core/about.html", context, context_instance=RequestContext(request))


def blog(request):
    context = {}
    return render_to_response("core/blog.html", context, context_instance=RequestContext(request))


def contact(request):
    context = {}
    return render_to_response("core/contact.html", context, context_instance=RequestContext(request))
