# Generated by Django 5.0.2 on 2024-03-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_remove_history_image_history_image_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=50)),
                ('image_path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]