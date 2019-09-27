from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Player
# Create your views here.
def home_view(request, *args,**kwargs):
    queryset = Player.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "home.html", context)