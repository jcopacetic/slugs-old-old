# Generated by Django 4.2.4 on 2023-09-03 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ledger",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
        ),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("currency", models.IntegerField(default=0)),
                (
                    "dashboard",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="wallet", to="dashboard.dashboard"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LedgerItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "ledger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="item", to="wallet.ledger"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="ledger",
            name="wallet",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="ledger", to="wallet.wallet"
            ),
        ),
    ]
