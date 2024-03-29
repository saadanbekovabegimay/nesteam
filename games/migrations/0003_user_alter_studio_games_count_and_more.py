# Generated by Django 4.2.4 on 2023-08-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_studio'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='studio',
            name='games_count',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='studio',
            name='workers_count',
            field=models.PositiveIntegerField(),
        ),
    ]
