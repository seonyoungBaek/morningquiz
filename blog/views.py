from django.shortcuts import render
from django.db import models


def CategoryView(request, category_name):
    category_posts = models.Post.objects.filter(category=category_name)
    categories = models.Category.objects.all()
    return render(
        request,
        "articles/categories.html",
        {
            "category_name": category_name,
            "category_posts": category_posts,
            "categories": categories,
        },
    )