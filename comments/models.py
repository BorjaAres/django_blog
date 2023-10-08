from django.db import models
from django.contrib.auth import get_user_model  # Import the custom user model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from posts.models import Post
from user.models import User

# Create a model for Comments on posts Posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')  # Post to which the comment belongs
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the comment
    content = models.TextField()  # Content of the comment
    date = models.DateTimeField(auto_now_add=True)  # Date and time when the comment was created

    def __str__(self):
        return self.content + ' | ' + str(self.user) + ' | ' + str(self.post)
        # Return a string representation of the comment, including content, user, and associated post

