# Generated by Django 3.2.4 on 2021-10-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('disciplina', models.CharField(max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='core')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calificacion', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('alumnos', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
