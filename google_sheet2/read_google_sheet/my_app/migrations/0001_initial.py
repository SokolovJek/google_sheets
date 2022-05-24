# Generated by Django 4.0.4 on 2022-05-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
                ('prise_usd', models.IntegerField()),
                ('delivery_time', models.DateField()),
                ('price_ru', models.IntegerField()),
            ],
        ),
    ]
