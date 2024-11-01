# Generated by Django 5.1.2 on 2024-10-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('records', 'Records'), ('clothing', 'Clothing'), ('posters', 'Posters'), ('miscellaneous', 'Miscellaneous')], default='records', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
