# Generated by Django 3.1 on 2020-08-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10),
        ),
    ]
