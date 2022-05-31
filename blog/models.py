from django.db import models
from django.urls import reverse
from django.db import models as core_models



class Articles(models.Model):
    movie = "movie"
    drama = "drama"
    entertain = "entertain"

    CATEGORY_CHOICES = (
         (movie, "movie"),
         (drama, "drama"),
         (entertain, "entertain")
    )
 
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.CharField(
         max_length=20,
         choices=CATEGORY_CHOICES,
         default=movie
    )

    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_question')


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")