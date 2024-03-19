from django.shortcuts import render, get_object_or_404
from .models import BlogPage
# Create your views here.
def blog_category(request, category_slug):
    blog_categories = BlogPage.objects.filter(categories__slug=category_slug)
    return render(request, 'blog/blog_category.html', {'blog_categories': blog_categories })