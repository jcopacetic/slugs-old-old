# Generated by Django 4.2.4 on 2023-09-03 23:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0003_alter_shopitem_item_alter_useritem_item"),
        ("dashboard", "0005_alter_usershop_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usershop",
            name="items",
            field=models.ManyToManyField(blank=True, related_name="shops", to="items.shopitem"),
        ),
    ]
