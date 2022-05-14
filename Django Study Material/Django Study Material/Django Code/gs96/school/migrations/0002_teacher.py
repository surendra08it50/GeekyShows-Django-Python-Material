# Generated by Django 3.0.5 on 2020-06-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('empnum', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
