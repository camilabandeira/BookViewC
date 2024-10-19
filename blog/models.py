from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.templatetags.static import static

# Create your models here.
CATEGORY_CHOICES = (
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-Fiction'),
    ('mystery', 'Mystery'),
    ('fantasy', 'Fantasy'),
    ('biography', 'Biography'),
    ('history', 'History'),
    ('science', 'Science'),
    ('romance', 'Romance'),
    ('others', 'Others'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_post_image(self):
        return self.cover_image.url if self.cover_image else static('images/default_image_post.png')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'