# Generated by Django 5.0.3 on 2024-03-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('buy', 'buy'), ('rent', 'rent')], max_length=20, null=True),
        ),
    ]
