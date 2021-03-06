# Generated by Django 3.0.6 on 2020-12-24 23:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='razonSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Razon Social',
                'verbose_name_plural': 'Razones Sociales',
            },
        ),
        migrations.CreateModel(
            name='unidadOperativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('razonSocial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.razonSocial')),
            ],
            options={
                'verbose_name': 'Unidad Operativa',
                'verbose_name_plural': 'Unidades Operativas',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('lastnamep', models.CharField(max_length=30, verbose_name='Apellido Paterno')),
                ('lastnamem', models.CharField(max_length=30, verbose_name='Apellido Materno')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('ocupation', models.CharField(blank=True, max_length=30, verbose_name='Cargo')),
                ('TypeDoc', models.CharField(blank=True, choices=[('1', 'DNI'), ('2', 'Carnet Extranjeria')], max_length=1, verbose_name='Tipo Documento')),
                ('NroDoc', models.CharField(blank=True, max_length=8, verbose_name='Nro. Documento')),
                ('TypeCompany', models.CharField(blank=True, choices=[('1', 'Colaborador'), ('2', 'Contrata')], max_length=1, verbose_name='Tipo Empresa')),
                ('Contrata', models.CharField(max_length=70, null=True, verbose_name='Contrata')),
                ('Ruc', models.CharField(max_length=11, null=True, verbose_name='RUC')),
                ('is_solicitante', models.BooleanField(default=True, verbose_name='Es solicitante')),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('razonSocial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.razonSocial')),
                ('unidadOperativa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.unidadOperativa')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
