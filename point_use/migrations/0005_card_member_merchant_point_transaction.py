# Generated by Django 2.1.5 on 2019-02-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('point_use', '0004_delete_member'),
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
            options={
                'db_table': 'CRD_MASTER_MST',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbr_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('mdn_no', models.CharField(max_length=12)),
                ('birthday', models.CharField(max_length=8)),
                ('mbr_sts', models.CharField(choices=[('A', 'available member'), ('R', 'retired member')], max_length=10)),
                ('last_sales_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'MBR_MASTER_MST',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcht_no', models.CharField(max_length=9)),
                ('mcht_sts', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'MCT_MASTER_MST',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbr_id', models.CharField(max_length=10)),
                ('point_knd_cd', models.CharField(max_length=3)),
                ('point_amt', models.IntegerField()),
            ],
            options={
                'db_table': 'MBR_MEMPNT_TRN',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprv_dy', models.CharField(max_length=8)),
                ('aprv_tm', models.CharField(max_length=6)),
                ('rep_aprv_no', models.CharField(max_length=9)),
                ('slp_cd', models.CharField(max_length=2)),
                ('deal_amt', models.IntegerField()),
            ],
            options={
                'db_table': 'APR_DEALTR_TRN',
            },
        ),
    ]