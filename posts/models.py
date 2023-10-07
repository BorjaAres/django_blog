from django.db import models
from django.contrib.auth import get_user_model  # Import the custom user model
from django.contrib.auth.models import Permission
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_permissions(sender, **kwargs):
    from .models import Post  # import here to avoid circular import
    post_content_type = ContentType.objects.get_for_model(Post)
    Permission.objects.get_or_create(
        codename='add_post',
        name='Can add post',
        content_type=post_content_type,
    )

# Fetch the custom user model (typically used for the Author of the Post and Comment)
User = get_user_model()

# Create a model for posts Posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='posts_images',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'webp'])]  # Add allowed extensions here
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

