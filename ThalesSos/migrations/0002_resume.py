# Generated by Django 4.2.3 on 2023-10-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThalesSos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=100)),
                ('var_Y', models.CharField(max_length=100)),
                ('var_X', models.CharField(max_length=100)),
                ('finalMessage', models.CharField(max_length=100)),
            ],
        ),
    ]
