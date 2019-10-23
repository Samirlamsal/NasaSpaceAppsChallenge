# Generated by Django 2.2.3 on 2019-10-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('martian', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Composition', models.TextField()),
                ('Recreation', models.TextField()),
                ('Research', models.TextField()),
                ('Image', models.ImageField(upload_to='img/')),
                ('Diameter', models.CharField(max_length=50)),
                ('Distance', models.CharField(max_length=50)),
                ('Temperature', models.CharField(max_length=50)),
                ('Density', models.CharField(max_length=50)),
            ],
        ),
    ]