# Generated by Django 2.1.1 on 2018-09-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_service_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_colour',
            field=models.CharField(default='#ff7230', max_length=200),
            preserve_default=False,
        ),
    ]
