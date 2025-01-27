from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.templatetags.static import static
from django.db.models.signals import post_save
from django.dispatch import receiver
from urllib.parse import urlparse, urlunparse 


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
    excerpt = models.TextField(blank=True, null=True)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    cover_image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_post_image(self):
        if self.cover_image:
            url = self.cover_image.url
            parsed_url = urlparse(url)
            secure_url = urlunparse(('https',) + parsed_url[1:])
            return f"{secure_url}?q_auto,f_auto"
        return static('images/default_image_post.png')


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
