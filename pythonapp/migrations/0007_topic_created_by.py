# Generated by Django 4.0.4 on 2022-06-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0006_alter_topic_text_alter_topic_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='created_by',
            field=models.CharField(default='username', max_length=50),
        ),
    ]
