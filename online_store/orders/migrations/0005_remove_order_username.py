# Generated by Django 4.1 on 2022-08-22 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_order_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="username",
        ),
    ]
