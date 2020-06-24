from django.shortcuts import render
from django.views.generic import (TemplateView,ListView, DetailView)
from .models import *



class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(pubished_date__lte=timezone.now().order_by('-published_date'))

    # template_name = "TEMPLATE_NAME"

class PostDetailView(DetailView):
    model = Post
    template_name = "TEMPLATE_NAME"

