# Generated by Django 2.2.6 on 2019-11-23 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191123_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battery_capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Battery_capacity', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Battery_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Battery_type', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Os_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_catagory', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Sub_Catagories',
            },
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='battery_capacity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Battery_capacity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='battery_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Battery_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='os_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Os_name'),
            preserve_default=False,
        ),
    ]
