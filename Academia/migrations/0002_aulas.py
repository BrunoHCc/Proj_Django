# Generated by Django 4.1.6 on 2023-02-09 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academia.professor')),
            ],
        ),
    ]
