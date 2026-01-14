from django.shortcuts import render

def _site_context():
    # Site variables stored here for simplicity. Update values as needed.
    return {
        "REPO_URL": "https://github.com/ariafatah0711/maku",
        "REPO_NAME": "ariafatah0711/maku",
        "LIVE_DEMO_URL": "https://aria.my.id/maku/",
    }


def home(request):
    return render(request, "home.html", _site_context())


def contact(request):
    return render(request, "contact.html", _site_context())


def gallery(request):
    return render(request, "gallery.html", _site_context())
