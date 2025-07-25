# Generated by Django 5.2.2 on 2025-06-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('selected_subjects', models.JSONField()),
                ('selected_interests', models.JSONField()),
                ('selected_skills', models.JSONField()),
                ('recommended_career', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
