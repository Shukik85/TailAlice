from django import template
from home.models import HomePage

register = template.Library()


@register.inclusion_tag('home/tags/navbar_tag.html', takes_context=False)
def navbar(page):
    url = page.full_url
    while not page.is_site_root():
        page = page.get_parent()
    navbar = page.homepage.navbar
    return {
        'navbar': navbar,
        'url': url,
    }
