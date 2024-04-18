# Generated by Django 5.0.4 on 2024-04-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(blank=True, max_length=100, null=True)),
                ('item_desc', models.TextField(blank=True, max_length=500, null=True)),
                ('item_image', models.ImageField(blank=True, null=True, upload_to='item/')),
            ],
        ),
    ]
