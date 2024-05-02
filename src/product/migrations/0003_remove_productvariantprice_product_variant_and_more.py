# Generated by Django 4.2.11 on 2024-05-02 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_productvariantprice_product_variant_one_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariantprice',
            name='product_variant',
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='product_variant_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_one', to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='product_variant_three',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_three', to='product.productvariant'),
        ),
        migrations.AddField(
            model_name='productvariantprice',
            name='product_variant_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_two', to='product.productvariant'),
        ),
    ]
