from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Person

# Module-specific configurable constants.
TARGET_NICK = "kevr"  # The Person's nick we're focused on.


def homepage(request: HttpRequest) -> HttpResponse:
    """ Render the home page of the application. """
    person = Person.objects.filter(nick=TARGET_NICK).first()
    if not person:
        return render(request, "404.html", status=404)

    context = {"person": person}
    return render(request, "index.html", context=context)
