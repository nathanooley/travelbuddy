from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.travelbuddy.urls', namespace='travels')),
]
