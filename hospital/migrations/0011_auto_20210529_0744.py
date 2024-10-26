# Generated by Django 3.2.3 on 2021-05-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20210529_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalbase',
            name='medico',
        ),
        migrations.AddField(
            model_name='hospitalbase',
            name='medico',
            field=models.ManyToManyField(to='hospital.Medico'),
        ),
    ]