# Generated by Django 4.2.4 on 2023-09-04 03:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0004_shopitem_amount_shopitem_in_market"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="useritem",
            name="user",
        ),
    ]
