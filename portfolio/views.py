from django.shortcuts import render
from .models import PortfolioPage
# Create your views here.
def project_category(request, category_slug):

        project_categories = PortfolioPage.objects.filter(categories__slug=category_slug)
        return render(request, 'portfolio/portfolio_index_page.html', {'project_categories': project_categories })
 

