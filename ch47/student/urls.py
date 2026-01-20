from django.urls import path
from .views import setsession, getsession, delsession, flushsession, sessionmethodsinview, sessionmethodsintemplate, sessionclear, settestcookie, checktestcookie, deltestcookie

urlpatterns = [
    path('set/', setsession, name="setsession"),
    path('get/', getsession, name="getsession"),
    path('del/', delsession, name="delsession"),
    path('flush/', flushsession, name="flushsession"),
    path('inview/', sessionmethodsinview, name="sessionmethodsinview"),
    path('intemplate/', sessionmethodsintemplate,
         name="sessionmethodsintemplate"),
    path('clear/', sessionclear, name="sessionclear"),
    
    path('settest/', settestcookie, name="settestcookie"),
    path('checktest/', checktestcookie, name="checktestcookie"),
    path('deltest/', deltestcookie, name="deltestcookie"),
]
