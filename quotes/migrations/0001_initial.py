# Generated by Django 3.2.25 on 2024-08-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('mood', models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('stressed', 'Stressed'), ('motivated', 'Motivated')], max_length=20)),
                ('category', models.CharField(choices=[('inspirational', 'Inspirational'), ('love', 'Love'), ('humor', 'Humor'), ('wisdom', 'Wisdom')], max_length=20)),
            ],
        ),
    ]