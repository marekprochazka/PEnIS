# Generated by Django 3.2.7 on 2021-09-28 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sleepover_form', '0009_rename_shoppinglist_shoppingitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoppingItem',
        ),
        migrations.DeleteModel(
            name='TypeUrgency',
        ),
    ]
