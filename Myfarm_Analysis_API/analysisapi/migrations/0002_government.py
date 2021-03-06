# Generated by Django 2.2 on 2019-04-25 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analysisapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
