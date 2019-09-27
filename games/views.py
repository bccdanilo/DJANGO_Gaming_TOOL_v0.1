from django.shortcuts import render

# Create your views here.
def call_dio(request):
    return render(request, "jogos/dio.html",{})

def call_square(request, id):
    return render(request, "jogos/square.html",{})
