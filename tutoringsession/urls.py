from django.urls import path
from . import views

app_name = "tutoringsession"

urlpatterns = [
    path("", views.index, name="index"),
    path("friends/", views.friends_sessions, name="friends_sessions"),
    path("sessions/<int:session_id>/request/", views.request_session, name="request_session"),
]