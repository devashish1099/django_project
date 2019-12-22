# Generated by Django 2.2.7 on 2019-12-22 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_text', models.CharField(max_length=2000)),
                ('likes', models.IntegerField(default=0)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tray.Title')),
            ],
        ),
    ]