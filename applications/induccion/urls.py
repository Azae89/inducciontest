#
from django.urls import path
from . import views

app_name = "induccion_app"

urlpatterns = [ 
    path(
        'salasadmin/', 
        views.EventListView.as_view(),
        name='entry-lista',
    ),
    path(
        'create-session-token', 
        views.UpdateToken.as_view(),
        name='create-session',
    ),  
     path(
        'room-live/<int:room>/', 
        views.OpenRoom.as_view(),
        name='in-session',
    ),     
]
