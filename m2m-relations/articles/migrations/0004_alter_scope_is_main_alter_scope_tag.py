# Generated by Django 4.1.7 on 2023-03-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.tag', verbose_name='Раздел'),
        ),
    ]