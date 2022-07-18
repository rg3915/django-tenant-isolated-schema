# Generated by Django 4.0.6 on 2022-07-18 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TenantAwareModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('tenantawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                 parent_link=True, primary_key=True, serialize=False, to='tenant.tenantawaremodel')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('tenant.tenantawaremodel',),
        ),
    ]