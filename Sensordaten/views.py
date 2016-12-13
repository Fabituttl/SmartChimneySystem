from django.http import Http404
from .models import Sensorkits
from django.shortcuts import render
from  django.template import loader


def index(request):
    all_sensorkits = Sensorkits.objects.all()
    return render(request, 'sensordaten/index.html', {'all_sensorkits' : all_sensorkits})

#detail ist die Funktion, die die Unterseite jedes gewählten Sensorkits anzeigt
def detail(request,sensorkit_id):
    try:
        sensorkit = Sensorkits.objects.get(pk=sensorkit_id)
    except Sensorkits.DoesNotExist:
        raise Http404("Leider ist dieses Sensorkit nicht mehr installiert.")
    return render(request, 'sensordaten/detail.html', {'sensorkit' : sensorkit})