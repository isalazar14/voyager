# Generated by Django 4.2.2 on 2023-06-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='Unknown', max_length=16),
            preserve_default=False,
        ),
    ]
