from blog.models import PostCategory, Post, Tag
from portfolio.models import Category, Portfolio
from Profiles.models import Profile, Course, Project


def blog_context(request):
    post_category = PostCategory.objects.filter(is_draft=False)
    recent_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:4]
    tag = Tag.objects.filter(is_draft=False)
    return {'post_category': post_category, 'r_post': recent_post, 'tag': tag}

def portfolio_context(request):
    portfolio_category = Category.objects.filter(is_draft=False)
    portfolio = Portfolio.objects.filter(is_draft=False)
    return {'portfolio_category': portfolio_category, 'portfolio': portfolio}

def profile_context(request):
    profile_category  = Profile.objects.filter(is_draft = False)
    profile = Profile.objects.filter(is_draft = False)
    course_category = Course.objects.filter(is_draft=False)
    Project_category = Project.objects.filter(is_draft = False)
    return {'profile_category': Profile,'course_category':Course,'Project_category':Project}




