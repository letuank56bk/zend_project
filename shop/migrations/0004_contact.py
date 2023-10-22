# Generated by Django 4.2.5 on 2023-10-15 08:00

from django.db import migrations, models
import django.utils.timezone
import shop.custom_field


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_alter_plantingmethod_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("message", models.TextField()),
                ("contacted", shop.custom_field.CustomBooleanFieldContact()),
                ("message_admin", models.TextField(blank=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "verbose_name_plural": "Contact",
            },
        ),
    ]