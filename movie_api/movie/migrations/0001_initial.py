# Generated by Django 4.1.4 on 2022-12-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('date_released', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
