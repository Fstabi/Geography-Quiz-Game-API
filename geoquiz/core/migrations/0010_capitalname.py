# Generated by Django 4.0.10 on 2023-08-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_challenge_challenges'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('capital_name', models.CharField(max_length=100)),
                ('difficulty', models.IntegerField()),
            ],
        ),
    ]
