# Generated by Django 4.1.7 on 2023-03-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Date Filed')),
                ('description', models.TextField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('agency', models.CharField(choices=[('P', 'Police'), ('T', 'Transportation'), ('F', 'Fire'), ('H', 'Health'), ('S', 'Sanitation'), ('U', 'Utilities'), ('O', 'Other')], default=0, max_length=1)),
            ],
        ),
    ]