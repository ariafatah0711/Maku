from django.http import JsonResponse
from django.urls import path, include

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health/", health),                            # health check endpoint
    path("", include("web.urls")),                      # root page
    # path("api/", include("transactions.urls")),         # API endpoints
]
