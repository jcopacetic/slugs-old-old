# Generated by Django 4.2.4 on 2023-09-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0002_useritem_in_shop_shopitem"),
        ("dashboard", "0004_alter_usershop_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usershop",
            name="items",
            field=models.ManyToManyField(blank=True, null=True, related_name="shops", to="items.shopitem"),
        ),
    ]
