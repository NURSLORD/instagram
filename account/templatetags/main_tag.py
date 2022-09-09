from django import template
from account.models import User

register = template.Library()


@register.inclusion_tag('tags/photo.html')
def photo(username):
    user = User.objects.get(username=username)
    image = user.image.url
    return {'image': image}