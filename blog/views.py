from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # posts is the name of our queryset of Posts pulled from the database
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts':posts})