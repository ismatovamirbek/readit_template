# Generated by Django 5.1.6 on 2025-02-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='article_images/')),
                ('day', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=15)),
                ('info', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('read_minute', models.CharField(max_length=25)),
            ],
        ),
    ]
