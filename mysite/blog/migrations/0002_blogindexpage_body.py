# Generated by Django 4.2.10 on 2024-02-18 10:11

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
