# Generated by Django 3.2.7 on 2021-10-13 13:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('results', models.CharField(max_length=20, validators=[django.core.validators.int_list_validator])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questioning.testresult')),
                ('user_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questioning.user')),
            ],
        ),
    ]
