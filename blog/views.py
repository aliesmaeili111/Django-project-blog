from django.shortcuts import render,get_object_or_404
from . models import Article,Category
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from account.models import User

# Create your views here.

# def home(request,page=1):
#     articles_list = Article.objects.published()
#     paginator = Paginator(articles_list,4)
#     articles = paginator.get_page(page)
#     #page = request.GET.get('page')
#     context = {
#         'articles':articles, 

#     }
#     return render(request,'blog/home.html',context)

#class base view for articles
class ArticleList(ListView):
    # model = Article
    # templated_name = "blog/home.html"
    # context_objects_name ='articles'
    queryset = Article.objects.published()
    paginate_by = 4
   
# detail view
# def detail(request,slug):
#     context = {
#         'article':get_object_or_404(Article.objects.published() ,slug = slug),
#     }
#     return render(request,'blog/detail.html',context)
# class base view detail
class ArticleDetail(DetailView):
    def get_object (self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published() ,slug = slug)
        


# category
# def category(request,slug,page = 1):
#     category = get_object_or_404(Category,slug = slug ,status = True)
#     articles_list = category.articles.published()
#     paginator = Paginator(articles_list,3)
#     articles = paginator.get_page(page)
#     context = {
#         'category':category,
#         'articles':articles,
#     }
#     return render(request,'blog/category.html',context)
# class base view category 
class CategoryList(ListView):
    
    templated_name = "blog/category_list.html"
    context_objects_name = "category"
    paginate_by = 4
    
    
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(),slug = slug )
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
    
class AuthorList(ListView):
    
    templated_name = "blog/author_list.html"
    paginate_by = 4
    
    
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username = username )
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context