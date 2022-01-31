# Generated by Django 3.1 on 2020-11-23 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('especialidad', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Especialidades',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('genero', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Generos',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=9, unique=True)),
                ('celular', models.CharField(blank=True, max_length=10, unique=True)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.genero')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.especialidad')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.genero')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Medicos',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='imagen_original')),
                ('evaluacion_foto', models.CharField(default='No realizado la evaluación', max_length=200)),
                ('fecha', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.paciente')),
            ],
            options={
                'verbose_name': 'evaluacion',
                'verbose_name_plural': 'evaluaciones',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('codigo', models.CharField(max_length=10)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]