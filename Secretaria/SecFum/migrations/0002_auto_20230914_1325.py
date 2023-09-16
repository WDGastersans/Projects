# Generated by Django 3.2.20 on 2023-09-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SecFum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='color_piel',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='sexo',
        ),
        migrations.AddField(
            model_name='formulario',
            name='baja',
            field=models.BooleanField(default=False, verbose_name='Baja'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='cargo',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='formulario',
            name='femenino',
            field=models.BooleanField(default=False, verbose_name='Femenina'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='masculino',
            field=models.BooleanField(default=False, verbose_name='Masculino'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='matricula',
            field=models.BooleanField(default=False, verbose_name='Matricula'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='militancia',
            field=models.CharField(default=False, max_length=4),
        ),
        migrations.AddField(
            model_name='formulario',
            name='rematricula',
            field=models.BooleanField(default=False, verbose_name='Rematricula'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='tezblanco',
            field=models.BooleanField(default=False, verbose_name='Blanco'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='tezmestizo',
            field=models.BooleanField(default=False, verbose_name='Mestizo'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='teznegro',
            field=models.BooleanField(default=False, verbose_name='Negro'),
        ),
    ]