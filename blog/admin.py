from django.contrib import admin
from . models import Article,Category
# Register your models here.

admin.site.site_header = "وبلاگ"
# add delete post in admin
# admin.site.disable_action('delete_selected')
# end delete post
#actions for admin site published 
def make_published(modeladmin,request,queryset):
    rows_updated = queryset.update(status='p') # author = 1 means ali to all
    if rows_updated == 1 :
        message_bit = "منتشر شد"
    else:
        message_bit = " منتشر شدند"
    modeladmin.message_user(request,"{} مقاله {} .".format(rows_updated,message_bit))
        
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin,request,queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1 :
        message_bit = "پیش نویس شد"
    else:
        message_bit = " پیش نویس شدند"
    modeladmin.message_user(request,"{} مقاله {} .".format(rows_updated,message_bit))
make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


def make_category_false(modeladmin,request,queryset):
    rows_updated = queryset.update(status=False)
    if rows_updated == 1 :
        message_bit = "این دسته بندی نمایش داده نمی شود"
    else:
        message_bit = "   دسته بندی ها  نمایش داده نمی شود"
    modeladmin.message_user(request,"{} {} .".format(rows_updated,message_bit))
make_category_false.short_description = "  نمایش ندادن دسته بندی ها "

def make_category_true(modeladmin,request,queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1 :
        message_bit = "این دسته بندی نمایش داده می شود"
    else:
        message_bit = "   دسته بندی ها  نمایش داده می شود"
    modeladmin.message_user(request,"{} {} .".format(rows_updated,message_bit))
make_category_true.short_description = "  نمایش دادن دسته بندی ها "
# end actions

# Custom admin for model article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','author','slug','jpublish','status','category_to_str')
    list_filter = ('publish','status','author') 
    search_fields = ('title','descriptions')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status','-publish']
    actions = [make_published,make_draft]
    
  

admin.site.register(Article,ArticleAdmin)

# Custom admin for model Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','parent','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    actions = [make_category_false,make_category_true]

admin.site.register(Category,CategoryAdmin)