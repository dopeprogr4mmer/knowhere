# Generated by Django 2.2 on 2021-04-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('phone_number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Forms',
                'unique_together': {('name', 'url', 'phone_number')},
            },
        ),
    ]
