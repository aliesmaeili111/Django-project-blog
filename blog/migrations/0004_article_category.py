# Generated by Django 4.0.1 on 2022-01-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
