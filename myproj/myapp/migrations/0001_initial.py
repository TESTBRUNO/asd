# Generated by Django 4.2.10 on 2024-03-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('count', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
