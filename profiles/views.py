from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .forms import RawProductForm


# Create your views here.
def profile_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Player.objects.create(**my_form.cleaned_data)
            return redirect('../')
        else:
            print(my_form.errors)
    context = {
        "form":my_form
    }
    return render(request, "create.html",context)


def profile_remove_view(request, id):
    obj = get_object_or_404(Player, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "delete.html", context)