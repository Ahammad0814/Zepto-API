# Generated by Django 5.0.2 on 2024-03-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0007_baby_care_cleaning_electronics_grooming_home_needs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageSrc', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
    ]
