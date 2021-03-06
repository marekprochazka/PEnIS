# Generated by Django 3.2.7 on 2021-09-25 15:40

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sleepover_form', '0002_auto_20210921_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCoitusProbability',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('x_created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='x_created')),
                ('x_modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='x_modified')),
                ('identifier', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Identifier')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('order', models.IntegerField(default=1, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Type coitus probability',
                'verbose_name_plural': 'Type coitus probabilities',
            },
        ),
        migrations.AlterModelOptions(
            name='sleepoverrequest',
            options={'verbose_name': 'Sleepover request', 'verbose_name_plural': 'Sleepover requests'},
        ),
        migrations.AddField(
            model_name='sleepoverrequest',
            name='note',
            field=models.TextField(blank=True, max_length=1028, null=True, verbose_name='Note'),
        ),
    ]
