# Generated by Django 5.1.2 on 2024-10-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-MAIL'),
        ),
    ]
