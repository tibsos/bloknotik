from django.shortcuts import render

from .models import FutureFeature

def donate(request):

    future_features = FutureFeature.objects.all()

    external_features = future_features.filter(internal = False)
    internal_features = future_features.filter(internal = True)

    tbd_internal_features = internal_features.filter(completed = False)
    completed_internal_features = internal_features.filter(completed = True)

    tbd_external_features = external_features.filter(completed = False)
    completed_external_features = external_features.filter(completed = True)

    c = {}

    return render(request, 'donate/donate.html', c)