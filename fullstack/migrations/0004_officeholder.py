# Generated by Django 2.1.5 on 2019-01-27 22:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fullstack', '0003_auto_20190127_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officeholder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('term_start', models.DateField()),
                ('term_end', models.DateField()),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack.Office')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fullstack.Person')),
            ],
        ),
    ]
