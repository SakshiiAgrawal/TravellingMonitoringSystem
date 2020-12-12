# Generated by Django 3.1 on 2020-11-26 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_done', models.CharField(max_length=10)),
                ('test_result', models.CharField(max_length=10)),
                ('quarentined', models.CharField(max_length=10)),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaar_number', models.CharField(default='', max_length=15)),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('gender', models.CharField(default='', max_length=10)),
                ('phone_no', models.CharField(default='', max_length=10)),
                ('age', models.CharField(default='', max_length=3)),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('room_no', models.IntegerField()),
                ('room_type', models.CharField(max_length=10)),
                ('bill', models.IntegerField()),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=70)),
                ('dest', models.CharField(max_length=70)),
                ('tv_date', models.DateTimeField(blank=True, null=True)),
                ('transportation', models.CharField(max_length=40)),
                ('co_pass', models.IntegerField()),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('covid_days', models.CharField(max_length=20)),
                ('hosp_clean', models.CharField(max_length=10)),
                ('food_quality', models.CharField(max_length=20)),
                ('travel_exp', models.CharField(max_length=300)),
                ('improvement', models.CharField(max_length=300)),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
