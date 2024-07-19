from django.shortcuts import render

def home(request):
    if request.GET.get("name") and request.GET.get("choice"):
        name = request.GET.get("name")
        choice = request.GET.get("choice")
        msg = "name=" + name + " choice=" + choice
        return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")


































