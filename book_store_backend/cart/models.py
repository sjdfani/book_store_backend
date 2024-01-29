from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from books.models import Book
from django.utils import timezone


class PurchaseItem(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("User"),
        related_name="PurchaseItem_user",
    )
    book = models.ForeignKey(
        Book, on_delete=models.DO_NOTHING, verbose_name=_("Book"),
        related_name="PurchaseItem_book",
    )
    count = models.PositiveIntegerField(verbose_name=_("Count"), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price_of_one_book = models.PositiveIntegerField(
        verbose_name=_("Price of one Book"), default=0)
    date_of_payment = models.DateTimeField(
        verbose_name=_("Date of Payment"), null=True, blank=True)
    transaction_id = models.CharField(
        max_length=50, verbose_name=_("Transaction_ID"), null=True, blank=True)
    status = models.BooleanField(verbose_name=_("Status"), default=True)

    def __str__(self) -> str:
        return self.user.email

    def bought_done(self, transaction_id: str):
        self.price_of_one_book = self.book.price
        self.date_of_payment = timezone.now()
        self.status = False
        self.transaction_id = transaction_id
        self.save()
