from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {"name": "Bram", "class": "PBP KKI"}

    return render(request, "main.html", context)
