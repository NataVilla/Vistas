# Generated by Django 4.1.3 on 2023-01-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priorapp', '0003_rename_orden_ordendj_rename_orden_ordendj_ordenv'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
            ],
        ),
    ]
