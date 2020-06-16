# Generated by Django 3.0.7 on 2020-06-13 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20200613_0753'),
        ('home', '0004_auto_20200611_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regi_key',
            name='user',
        ),
        migrations.AddField(
            model_name='regi_key',
            name='cli',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='appointment.Client'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]