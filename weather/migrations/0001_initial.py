# Generated by Django 5.0.2 on 2024-03-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('degination', models.CharField(max_length=200)),
                ('timeperiod', models.CharField(max_length=100)),
                ('work_done', models.TextField()),
                ('score', models.CharField(max_length=50)),
                ('skill_set', models.TextField()),
            ],
        ),
    ]