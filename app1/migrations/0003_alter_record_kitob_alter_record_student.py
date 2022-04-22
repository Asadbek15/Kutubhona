# Generated by Django 4.0.3 on 2022-04-11 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_kitob_muallif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='kitob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitoblar_record', to='app1.kitob'),
        ),
        migrations.AlterField(
            model_name='record',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_record', to='app1.student'),
        ),
    ]
