# Generated by Django 4.2 on 2023-04-24 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom de la matière')),
                ('code', models.CharField(max_length=50, verbose_name='Code de la matière')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom du niveau')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Code du niveau')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom de la session')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SalleDeClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='MatiereCoef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coef', models.PositiveIntegerField(verbose_name='Coéficient')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.matiere')),
            ],
        ),
    ]
