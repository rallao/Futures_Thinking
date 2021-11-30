from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserEntries(models.Model):
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=350)
<<<<<<< HEAD
    img = models.CharField(max_length=250)
    video_url = models.CharField(max_length=250)
    date = models.DateField('Post Date')
=======
   
    img = models.CharField(max_length=250, blank=True)
    video = EmbedVideoField(blank=True)
    date = models.DateTimeField(auto_now=True)
>>>>>>> 543e3dbcf1f5b5528d5c70daa7cbeaf9a159b428
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} was created on {self.date} with the id of {self.id}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.id})
    

class AllEntries(models.Model):
    user_entries = models.ForeignKey(UserEntries, on_delete=models.CASCADE)

    def __str__(self):
        return f"This user entry is from {self.user_entries}"

# set email for login
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']

# user model extension
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=600)
    twitter = models.CharField(max_length=100)

    def __str__(self):
        return self.bio

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_id': self.id})