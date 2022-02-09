
from django import template
from .. models import Category,Article
from django.db.models import Count,Q
from datetime import datetime,timedelta
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ علی"



@register.inclusion_tag("blog/partials/category_navbar.html")
def catefory_navbar():
    return{
        'category':Category.objects.filter(status=True)
    }
    
    
    # start template tag sidebar in articles
@register.inclusion_tag("blog/partials/sidebar.html")
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    return {
        'articles':Article.objects.published().annotate(count=Count('hits',filter=Q(articlehit__created__gt=last_month))).order_by('-count','-publish')[:4],
        'title':'مقاله پربازدیدماه',
    }
    
@register.inclusion_tag("blog/partials/sidebar.html")
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label='blog',model="article").id
    return {
        'articles':Article.objects.published().annotate(count=Count('comments',filter=Q(comments__posted__gt=last_month) and Q(comments__content_type_id = content_type_id ))).order_by('-count','-publish')[:4],
        'title':'مقاله داغ ما',
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