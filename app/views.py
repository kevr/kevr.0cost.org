from django.db.models.functions import Length
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.models import Person

# Module-specific configurable constants.
TARGET_NICK = "kevr"  # The Person's nick we're focused on.


def get_person(nick: str) -> Person:
    return Person.objects.filter(nick=TARGET_NICK).first()


def make_context(request: HttpRequest) -> dict[str, str]:
    return {"path": request.path}


def columns_to_rows(columns: list) -> list[list[str]]:
    """ Split an arbitrary number of columns into enough
    rows to hold three columns worth of data. """
    output = []
    for i in range(0, 3):
        current = []
        for j in range(0, int(len(columns) / 3)):
            current.append(columns[i + j * 3])
        output.append(current)
    return output


def homepage(request: HttpRequest) -> HttpResponse:
    """ Render the home page of the application. """
    context = make_context(request)
    person = get_person(TARGET_NICK)
    if not person:
        return render(request, "404.html", status=404)

    context["person"] = person

    technology_set = person.technology_set.order_by(
        Length("name").asc()).all()
    context["technologies"] = columns_to_rows(technology_set)

    protocol_set = person.protocol_set.order_by(
        Length("name").asc()).all()
    context["protocols"] = columns_to_rows(protocol_set)

    return render(request, "index.html", context=context)


def projects(request: HttpRequest) -> HttpResponse:
    """ Render the Projects page. """
    context = make_context(request)
    person = get_person(TARGET_NICK)
    if not person:
        return render(request, "404.html", status=404)

    context["person"] = person
    context["projects"] = person.project_set.all()
    return render(request, "projects.html", context=context)
