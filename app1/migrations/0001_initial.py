# Generated by Django 4.0.3 on 2022-04-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('sana', models.DateField(blank=True)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('janr', models.CharField(choices=[('1', 'Badiy'), ('2', 'Ilmiy'), ('3', 'Fantastik'), ('4', 'Dokumental'), ('5', 'Tarihiy')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=15)),
                ('tirik', models.BooleanField(default='Tirik')),
                ('yosh', models.PositiveSmallIntegerField()),
                ('kitoblar_soni', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=15)),
                ('guruh', models.PositiveSmallIntegerField(blank=True)),
                ('kitoblar_soni', models.IntegerField(blank=True, default='0')),
                ('bitiruvchi', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.kitob')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.muallif'),
        ),
    ]
