# Generated by Django 5.0.2 on 2024-03-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouanis', '0002_annonce_demandeannonce_demandedecomptevoyageur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediteur',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediteur',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediteur',
            name='mot_de_passe',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediteur',
            name='nom',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediteur',
            name='prenom',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyageur',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyageur',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyageur',
            name='mot_de_passe',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyageur',
            name='nom',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyageur',
            name='prenom',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
