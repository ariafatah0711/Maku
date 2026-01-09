from django.http import JsonResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health/", health),                            # health check endpoint
    path("", include("web.urls")),                      # web app (home, contact)
    path("app/", include("app.urls")),                  # app module (transactions)
]
