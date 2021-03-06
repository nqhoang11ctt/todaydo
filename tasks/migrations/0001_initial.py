# Generated by Django 2.1.5 on 2019-02-07 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('done', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('high', 'High'), ('low', 'Low')], default='low', max_length=5)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
