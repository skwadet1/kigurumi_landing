# Generated by Django 2.2.7 on 2019-12-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scumapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('userpic', models.ImageField(upload_to='userpics/')),
                ('reviewpic', models.ImageField(upload_to='reviewpics/')),
                ('likes', models.CharField(max_length=30)),
                ('review', models.TextField(max_length=500)),
            ],
        ),
    ]
