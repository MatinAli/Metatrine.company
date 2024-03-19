from django.shortcuts import render, get_object_or_404
<<<<<<< HEAD
from .models import BlogPage
=======
from .models import Comment, BlogPage
from .forms import CommentForm
>>>>>>> 9a20156 (initial commit)

# Create your views here.
def blog_category(request, category_slug):
    blog_categories = BlogPage.objects.filter(categories__slug=category_slug)
<<<<<<< HEAD
    return render(request, 'blog/blog_category.html', {'blog_categories': blog_categories })
=======
    return render(request, 'blog/blog_category.html', {'blog_categories': blog_categories })

# def submit_comment(request, page_id):

#     if request.method == 'POST':
#         # A comment was posted
#         form = CommentForm(request.POST) 
#         if form.is_valid():
#             # create a comment but don't save it to database yet
#             comment=form.save(commit=False)
#             # Assign the current post to the comment
#             comment.page_id = page_id
#             # save the comment to database
#             comment.save()
#             return redirect('page_detail', page_id)
#     else:
#         form = CommentForm()
#     return render(request,'blog/blog_page.html', {'form':form})

# def page_detail(request, page_id):

#     page = get_object_or_404(Page, id=page_id)
#     comments=page.comments.all()
#     return render(request, 'blog/blog_page.html', {'page':page, 'comments':comments})


def blog_post_navigation(request, blog_page_slug):

    current_post = get_object_or_404(BlogPage, slug=blog_page_slug)

    # Retrieve next and previous posts
    # Get the previous post
    previous_post = BlogPage.objects.filter(pub_date__lt=current_post.pub_date).order_by('-pub_date').first()

    # Get the next post
    next_post = BlogPage.objects.filter(pub_date__gt=current_post.pub_date).order_by('pub_date').first()

    return render(
        request,
        'blog/blog_page.html', {
        'next_post': next_post,
        'previous_post': previous_post
    })
>>>>>>> 9a20156 (initial commit)
