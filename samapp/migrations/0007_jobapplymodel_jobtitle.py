# Generated by Django 4.1.5 on 2023-01-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0006_remove_jobapplymodel_email2'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplymodel',
            name='jobtitle',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
