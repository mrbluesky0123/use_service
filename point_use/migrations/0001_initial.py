# Generated by Django 2.1.5 on 2019-01-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crd_no', models.CharField(max_length=16)),
                ('mbr_id', models.CharField(max_length=10)),
                ('crd_sts', models.CharField(max_length=20)),
                ('crd_cd', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbr_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('mdn_no', models.CharField(max_length=12)),
                ('birthday', models.CharField(max_length=8)),
                ('mbr_sts', models.CharField(max_length=10)),
                ('last_sales_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcht_no', models.CharField(max_length=9)),
                ('mcht_sts', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbr_id', models.CharField(max_length=10)),
                ('point_knd_cd', models.CharField(max_length=3)),
                ('point_amt', models.IntegerField()),
            ],
        ),
    ]
