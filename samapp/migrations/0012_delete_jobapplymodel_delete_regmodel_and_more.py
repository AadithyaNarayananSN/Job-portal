# Generated by Django 4.1.5 on 2023-01-28 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0011_delete_viewappliedusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='jobapplymodel',
        ),
        migrations.DeleteModel(
            name='regmodel',
        ),
        migrations.DeleteModel(
            name='userdetailsmodel',
        ),
        migrations.DeleteModel(
            name='vaccancyuploadmodel',
        ),
        migrations.DeleteModel(
            name='wishlistmodel',
        ),
    ]
