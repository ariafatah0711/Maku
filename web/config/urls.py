from django.http import JsonResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("health/", health),                            # health check endpoint
    path("", include("web.urls")),                      # root page
    # path("api/", include("transactions.urls")),       # API endpoints
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
