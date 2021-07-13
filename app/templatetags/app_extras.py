import re

from django import template
from django.db.models.functions import Length

register = template.Library()


@register.simple_tag()
def by_length(queryset, column: str):
    return queryset.order_by(Length(column).asc())


@register.filter("phone_format")
def phone_format(phone: str) -> str:
    match = re.match(r'^(\d)(\d{3})(\d{3})(\d{4})$', phone)
    if not match:
        raise ValueError(f"Invalid phone format: '{phone}'.")

    nation = match.group(1)
    area = match.group(2)
    lhs = match.group(3)
    rhs = match.group(4)
    return f"{nation} ({area}) {lhs}-{rhs}"
