from django.urls import path, include

urlpatterns = [
    path('', include('weather_app.urls'))
]
