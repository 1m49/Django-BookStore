# Generated by Django 4.2.4 on 2023-09-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_comment_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True, verbose_name='این کتاب و پیشنهاد میکنی؟'),
        ),
    ]
