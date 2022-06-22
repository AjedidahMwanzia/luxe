from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render (request,'index.html')