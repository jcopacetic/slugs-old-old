# Generated by Django 4.2.4 on 2023-09-03 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(max_length=500)),
                ("value", models.IntegerField(default=0)),
                ("rarity", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.item",
                    ),
                ),
                ("health", models.IntegerField(default=50)),
            ],
            bases=("items.item",),
        ),
        migrations.CreateModel(
            name="UserItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="created", to="items.item"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="items", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
