# Generated by Django 5.1.2 on 2024-10-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rooms',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]