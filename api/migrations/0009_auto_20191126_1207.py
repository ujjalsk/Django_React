# Generated by Django 2.2.3 on 2019-11-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191126_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='address',
            field=models.TextField(default='', max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='cart_item_quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='mobile_number',
            field=models.CharField(default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='pin',
            field=models.CharField(default='', max_length=120, null=True),
        ),
    ]
