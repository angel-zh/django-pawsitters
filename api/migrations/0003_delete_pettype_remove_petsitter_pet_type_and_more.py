# Generated by Django 4.1.3 on 2022-11-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_petsitter_from_date_remove_petsitter_pet_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PetType',
        ),
        migrations.RemoveField(
            model_name='petsitter',
            name='pet_type',
        ),
        migrations.AddField(
            model_name='petsitter',
            name='bird',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='cat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='dog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='reptile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='petsitter',
            name='small_animal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='petsitter',
            name='dog_walking',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='petsitter',
            name='medicine',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='petsitter',
            name='pet_sitting',
            field=models.BooleanField(default=False),
        ),
    ]