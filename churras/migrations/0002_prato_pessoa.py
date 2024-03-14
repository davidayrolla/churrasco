# Generated by Django 4.1.7 on 2023-06-06 23:01

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        # ('pessoas', '0002_alter_pessoa_nome'),
        ('churras', '0001_initial'),
    ]

    operations = [
        # migrations.AddField(
        #      model_name='prato',
        #      name='pessoa',
        #      # field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
        #      # preserve_default=False,
        #  ),

        # Esse código veio do arquivo 0005 (recortado e colado)
        migrations.AddField(
            model_name='prato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]