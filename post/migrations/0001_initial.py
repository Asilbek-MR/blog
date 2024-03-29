# Generated by Django 4.1.7 on 2023-04-03 05:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(choices=[('healthy', 'HEALTHY'), ('image', 'photo'), ('programming', 'PROGRAMMING'), ('productive', 'PRODUCTIVE'), ('desigin', 'DESIGIN'), ('self_improvement', 'Self_Improvement')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gmail', models.EmailField(blank=True, max_length=254)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('content', ckeditor.fields.RichTextField()),
                ('extra_like', models.IntegerField(default=0)),
                ('dis_extra_like', models.IntegerField(default=0)),
                ('main_article', models.BooleanField()),
                ('global_news', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='post.category')),
            ],
        ),
    ]
