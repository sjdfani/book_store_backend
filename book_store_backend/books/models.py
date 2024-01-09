from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


class BookLanguage(models.TextChoices):
    ENG = ("eng", "Eng")
    PER = ("per", "Per")


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    author = models.CharField(_("Author"), max_length=255)
    rating = models.FloatField(verbose_name=_("Rating"), default=0.0)
    number_of_pages = models.PositiveIntegerField(
        verbose_name=_("Number_of_Pages"), default=0)
    language = models.CharField(
        _("Language"), max_length=3, choices=BookLanguage.choices)
    description = models.TextField(verbose_name=_("Description"))
    price = models.PositiveIntegerField(verbose_name=_("Price"), default=0)
    publish = models.BooleanField(verbose_name=_("Publish"), default=False)

    def __str__(self) -> str:
        return self.title


class SaveItem(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        verbose_name=_("User"), related_name="SaveItem_user")
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, verbose_name=_("Book"),
        related_name="SaveItem_book")
