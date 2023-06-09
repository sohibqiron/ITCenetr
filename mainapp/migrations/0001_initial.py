# Generated by Django 4.0.3 on 2022-03-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('direction_teaching', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('country', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to='mentor')),
                ('salary', models.FloatField()),
            ],
        ),
    ]
