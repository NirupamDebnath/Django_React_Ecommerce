# Generated by Django 3.0.4 on 2020-06-25 22:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ecommerce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('image', models.ImageField(upload_to=ecommerce.models.upload_image_path)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('added_on', models.DateField(default=django.utils.timezone.now)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Category')),
            ],
        ),
    ]