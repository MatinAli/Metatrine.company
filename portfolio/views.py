from django.shortcuts import render
from .models import PortfolioCategory
# Create your views here.
def category_filter(request):
    categories = PortfolioCategory.objects.all() 
    return render(request, 'portfolio/portfolio_index_page.html', {'categories': categories })