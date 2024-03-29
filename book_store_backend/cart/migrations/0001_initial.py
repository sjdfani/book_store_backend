# Generated by Django 5.0 on 2024-01-09 07:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Count')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price_of_one_book', models.FloatField(default=0.0, verbose_name='Price of one Book')),
                ('date_of_payment', models.DateTimeField(blank=True, null=True, verbose_name='Date of Payment')),
                ('transaction_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Transaction_ID')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='PurchaseItem_book', to='books.book', verbose_name='Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseItem_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('purchase_items', models.ManyToManyField(to='cart.purchaseitem', verbose_name='Purchase Items')),
            ],
        ),
    ]
