# Generated by Django 3.2 on 2023-01-31 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20230131_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(default='no-image.jpg', height_field='imageheight', upload_to='static/images/products/20230131-101256', width_field='imagewidth'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230131 - 101256'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230131 - 101256'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230131 - 101256'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default='no-image.jpg', null=True, upload_to='static/images/products/20230131 - 101256'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]