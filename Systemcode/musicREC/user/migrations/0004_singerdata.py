# Generated by Django 4.1.2 on 2022-10-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_musicdata_na_musicdata_nb_musicdata_nc_musicdata_nd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer', models.CharField(max_length=100)),
                ('PA', models.FloatField(default=0)),
                ('PE', models.FloatField(default=0)),
                ('PD', models.FloatField(default=0)),
                ('PH', models.FloatField(default=0)),
                ('PG', models.FloatField(default=0)),
                ('PB', models.FloatField(default=0)),
                ('PK', models.FloatField(default=0)),
                ('NA', models.FloatField(default=0)),
                ('NB', models.FloatField(default=0)),
                ('NJ', models.FloatField(default=0)),
                ('NH', models.FloatField(default=0)),
                ('PF', models.FloatField(default=0)),
                ('NI', models.FloatField(default=0)),
                ('NC', models.FloatField(default=0)),
                ('NG', models.FloatField(default=0)),
                ('NE', models.FloatField(default=0)),
                ('ND', models.FloatField(default=0)),
                ('NN', models.FloatField(default=0)),
                ('NK', models.FloatField(default=0)),
                ('NL', models.FloatField(default=0)),
                ('PC', models.FloatField(default=0)),
            ],
        ),
    ]
