# Generated by Django 4.0.6 on 2022-07-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subjects', models.ManyToManyField(blank=True, related_name='students', to='school_app.subject')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]