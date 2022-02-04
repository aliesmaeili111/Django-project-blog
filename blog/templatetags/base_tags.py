from atexit import register
from django import template
from .. models import Category
register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ علی"



@register.inclusion_tag("blog/partials/category_navbar.html")
def catefory_navbar():
    return{
        'category':Category.objects.filter(status=True)
    }
    
    
@register.inclusion_tag('registration/partials/link.html')
def link(request,link_name,content,classes):
    return{
        'request':request,
        'link_name':link_name,
        'link':f'account:{link_name}',
        'content':content,
        'classes':classes,
    }