# Generated by Django 2.2.3 on 2019-10-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]