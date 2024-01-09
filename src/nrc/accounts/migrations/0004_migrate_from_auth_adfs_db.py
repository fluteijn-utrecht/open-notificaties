# Generated by Django 3.2.13 on 2022-06-21 06:41


from django.db import migrations


class Migration(migrations.Migration):
    # migration is made no-op in the 1.6.x release series - on 1.4.x this copied
    # over the configuration from auth_adfs to mozilla_oidc.
    # This migration is kept for historical reasons to not mess with the migration
    # history of existing installs. See #1139 for more context.
    dependencies = [
        ("accounts", "0003_add_adfs_admin_index"),
        ("mozilla_django_oidc_db", "0008_auto_20220422_0849"),
    ]

    operations = []
