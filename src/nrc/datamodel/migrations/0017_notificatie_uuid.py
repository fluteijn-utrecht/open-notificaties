# Generated by Django 3.2.17 on 2023-06-30 14:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0016_alter_abonnement_callback_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificatie",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                help_text="Unique resource identifier (UUID4)",
                unique=True,
            ),
        ),
    ]
