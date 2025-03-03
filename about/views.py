from django.shortcuts import render
from .models import Team, Clients


def index(request):
    my_team = Team.objects.all()
    client = Clients.objects.all()
    context = {
        "my_team": my_team,
        "client": client
    }
    return render(request, "about.html", context)

