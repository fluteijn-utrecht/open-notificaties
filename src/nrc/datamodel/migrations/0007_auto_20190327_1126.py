# Generated by Django 2.1.7 on 2019-03-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("datamodel", "0006_auto_20190327_1101")]

    operations = [
        migrations.AddField(
            model_name="notificatieresponse",
            name="exception",
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name="notificatieresponse",
            name="response_status",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
