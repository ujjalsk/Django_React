# Generated by Django 2.2.6 on 2019-11-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191123_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='sub_catagory',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
