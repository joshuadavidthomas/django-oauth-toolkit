# Generated by Django 5.0.7 on 2024-07-29 23:13

import oauth2_provider.models
from django.db import migrations, models
from oauth2_provider.settings import oauth2_settings

def forwards_func(apps, schema_editor):
    """
    Forward migration touches every "old" accesstoken.token which will cause the checksum to be computed.
    """
    AccessToken = apps.get_model(oauth2_settings.ACCESS_TOKEN_MODEL)
    accesstokens = AccessToken._default_manager.all()
    for accesstoken in accesstokens:
        accesstoken.save(update_fields=['token_checksum'])


class Migration(migrations.Migration):
    dependencies = [
        ("oauth2_provider", "0011_refreshtoken_token_family"),
        migrations.swappable_dependency(oauth2_settings.ACCESS_TOKEN_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="accesstoken",
            name="token_checksum",
            field=oauth2_provider.models.TokenChecksumField(blank=True, null=True, max_length=64),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="token",
            field=models.TextField(),
        ),
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='accesstoken',
            name='token_checksum',
            field=oauth2_provider.models.TokenChecksumField(blank=False, max_length=64,  db_index=True, unique=True),
        ),
    ]