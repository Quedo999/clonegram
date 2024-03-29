from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for clone_gram.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    GENDER_TYPE = [
        ('M', 'Male'), ('F', 'Female'), ('C', 'Custom'), ('N', 'Prefer not to say')
    ]

    #: First and last name do not cover name patterns around the globe
    profile_img = models.ImageField(blank=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_TYPE, max_length=255)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
