from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page
from wagtail.contrib.search_promotions.models import Query
from blog.models import BlogPage


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = BlogPage.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = BlogPage.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    recent_posts = [page.get_recent_posts() for page in search_results.object_list]

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
            "recent_posts": recent_posts,
        },
    )


def get_recent_posts(self):

    max_count = 4

    recent_posts = BlogPage.objects.all().order_by('-first_published_at')[:max_count]

    context['recent_posts']=recent_posts
    
    return context

