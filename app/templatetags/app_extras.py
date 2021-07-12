from django import template
from django.db.models.functions import Length

register = template.Library()


@register.simple_tag()
def by_length(queryset, column: str):
    return queryset.order_by(Length(column).desc())
