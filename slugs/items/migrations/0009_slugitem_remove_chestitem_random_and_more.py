# Generated by Django 4.2.4 on 2023-09-04 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0008_alter_chestitem_random"),
    ]

    operations = [
        migrations.CreateModel(
            name="SlugItem",
            fields=[
                (
                    "useritem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="items.useritem",
                    ),
                ),
                ("random_number", models.IntegerField(default=0)),
            ],
            bases=("items.useritem",),
        ),
        migrations.RemoveField(
            model_name="chestitem",
            name="random",
        ),
        migrations.AddField(
            model_name="chestitem",
            name="random_number",
            field=models.IntegerField(default=0),
        ),
    ]
