# Generated by Django 5.0.3 on 2024-04-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_type',
            field=models.CharField(choices=[('YT', 'Youtube'), ('IG', 'Instagram'), ('Other', 'Other')], max_length=10),
        ),
    ]
