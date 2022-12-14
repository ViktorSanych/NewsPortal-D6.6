# Generated by Django 4.1.1 on 2022-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Категория статьи', 'verbose_name_plural': 'Категории статьи'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='post_category',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]
