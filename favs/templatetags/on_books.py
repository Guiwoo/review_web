from django import template
from favs import models as favs_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_books(context, book):
    if context.request.user.is_authenticated:
        user = context.request.user
        the_favs = favs_models.FavList.objects.get_or_none(created_by=user)
        return book in the_favs.books.all()
