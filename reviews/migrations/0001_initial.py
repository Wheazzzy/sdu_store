# Generated by Django 4.2 on 2023-04-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.category')),
            ],
        ),
    ]