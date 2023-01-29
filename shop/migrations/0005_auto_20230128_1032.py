# Generated by Django 3.2 on 2023-01-28 10:32

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('shop', '0004_auto_20230128_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='counted_view',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='counted_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20230128-103208', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230128 - 103208'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230128 - 103208'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230128 - 103208'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230128 - 103208'),
        ),
    ]
