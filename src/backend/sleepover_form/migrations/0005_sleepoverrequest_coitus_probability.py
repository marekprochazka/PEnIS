# Generated by Django 3.2.7 on 2021-09-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sleepover_form', '0004_alter_typecoitusprobability_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sleepoverrequest',
            name='coitus_probability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sleepover_form.typecoitusprobability', verbose_name='Coitus probability'),
        ),
    ]
