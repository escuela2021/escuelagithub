# Generated by Django 3.2.4 on 2021-11-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina'),
        ),
    ]
