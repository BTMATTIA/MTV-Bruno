# Generated by Django 4.1.4 on 2022-12-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DesafioMTVBruno', '0002_remove_persona_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.CharField(max_length=255),
        ),
    ]
