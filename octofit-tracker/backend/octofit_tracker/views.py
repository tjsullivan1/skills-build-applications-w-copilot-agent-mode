from django.http import JsonResponse


def api_root(request):
    return JsonResponse(
        {
            "message": "Welcome to the OctoFit Tracker API!",
            "url": "https://laughing-space-yodel-6rg754jqqc5476.github.dev/-8000.app.github.dev",
        }
    )
