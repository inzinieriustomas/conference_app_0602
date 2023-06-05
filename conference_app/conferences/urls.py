from django.urls import path

from conferences.views import ConferenceListView, ConferenceDetailView

urlpatterns = [
    path("", ConferenceListView.as_view()),
    path("<int:pk>/", ConferenceDetailView.as_view, name = ())
]