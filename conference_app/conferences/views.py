from django.shortcuts import render
from django.views.generic import ListView, DetailView

from conferences.models import Conference


# Create your views here.
class ConferenceListView (ListView):
    model = Conference


class ConferenceDetailView(DetailView):
    model = Conference
