# Generated by Django 4.0 on 2021-12-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0007_book_sessionmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='meetingInfo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='meetingName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
