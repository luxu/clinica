# Generated by Django 3.2.3 on 2021-05-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_auto_20210529_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='hospital',
        ),
        migrations.AlterField(
            model_name='hospitalbase',
            name='medico',
            field=models.ManyToManyField(related_name='medicos_do_hospital', to='hospital.Medico'),
        ),
    ]
