<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-06-30 10:50
=======
# Generated by Django 3.2.5 on 2021-07-01 12:13
>>>>>>> e990b36cd75b3abe2e39b3046d6f849ae831c0c3

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Item',
=======
            name='item',
>>>>>>> e990b36cd75b3abe2e39b3046d6f849ae831c0c3
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
