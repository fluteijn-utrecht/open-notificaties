# Generated by Django 2.1.7 on 2019-03-27 11:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0005_kanaal_filters")]

    operations = [
        migrations.AlterField(
            model_name="kanaal",
            name="filters",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=100),
                blank=True,
                default=list,
                help_text="Comma-separated list of filters of the kanaal",
                size=None,
                verbose_name="filters",
            ),
        )
    ]
