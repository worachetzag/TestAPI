# Generated by Django 4.0.1 on 2022-01-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.CharField(max_length=200)),
                ('heart_rate', models.IntegerField()),
                ('walk_count', models.IntegerField()),
            ],
        ),
    ]