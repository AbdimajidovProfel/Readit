from django.db import models
from django.urls import reverse


class ContactModel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=44)
    phone = models.CharField(verbose_name="Phone", max_length=55)
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(verbose_name="Subject", max_length=222)
    message = models.TextField(verbose_name="Message", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.name}: {self.phone}"

    def get_absolute_url(self):
        return reverse("contact")

