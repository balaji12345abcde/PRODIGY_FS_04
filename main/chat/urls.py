from django.urls import path
from .views import HomePage,RoomPage
urlpatterns=[
    path('',HomePage,name="home"),
    path('<str:room_name>/<str:user_name>',RoomPage,name="room"),
]