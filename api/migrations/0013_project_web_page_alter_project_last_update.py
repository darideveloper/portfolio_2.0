# Generated by Django 4.0.4 on 2023-03-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_tag_remove_userbadge_badge_remove_userbadge_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='web_page',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateField(auto_now_add=True),
        ),
    ]
