# Generated by Django 4.1.4 on 2023-03-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_rename_akhil_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='signinpeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=22)),
                ('password', models.CharField(max_length=22)),
            ],
        ),
    ]