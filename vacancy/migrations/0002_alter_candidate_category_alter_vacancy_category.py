# Generated by Django 4.1 on 2022-08-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='vacancy.category'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancy.category'),
        ),
    ]
