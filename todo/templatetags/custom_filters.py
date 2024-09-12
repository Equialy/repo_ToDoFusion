from django import template

from todo.models import Categories
import todo.views as views

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})
@register.inclusion_tag('todo/categories.html')
def categories(cat_selected = 0):
    cats  = Categories.objects.all()

    return {"cats": cats, 'cat_selected':cat_selected}
