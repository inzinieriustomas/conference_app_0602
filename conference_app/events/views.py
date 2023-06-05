from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView

from .models import Event


# Create your views here.
class EventDetailView(DetailView):
    model = Event
    context_object_name = "renginys"


def register_visitor(request, renginio_id ):
    event = get_object_or_404 (Event,id = renginio_id)
    event.visitors += 1
    event.save()


    return redirect(f"/events/{renginio_id}")
    # return HttpResponse( event.title)