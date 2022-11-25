# Generated by Django 4.1.3 on 2022-11-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_petsitter_id_alter_petsitter_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petsitter',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='petsitter',
            name='to_date',
        ),
        migrations.AddField(
            model_name='petsitter',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
