# Generated by Django 4.1.2 on 2022-10-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="url",
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="date",
            field=models.DateField(),
        ),
    ]