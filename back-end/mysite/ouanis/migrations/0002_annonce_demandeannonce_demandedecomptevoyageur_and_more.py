# Generated by Django 5.0.2 on 2024-03-15 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ouanis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lieu_depart', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('poids_max', models.IntegerField()),
                ('prix_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DemandeAnnonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('statut', models.CharField(choices=[('en_attente', 'En Attente'), ('accepte', 'Accepté'), ('rejete', 'Rejeté')], default='en_attente', max_length=20)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DemandeDeCompteVoyageur',
            fields=[
                ('expediteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ouanis.expediteur')),
                ('est_approuve', models.BooleanField(default=False)),
                ('date_de_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AnnonceDeColies',
        ),
        migrations.DeleteModel(
            name='AnnonceDeCorier',
        ),
        migrations.RenameField(
            model_name='expediteur',
            old_name='nom',
            new_name='numero_telephone',
        ),
        migrations.RenameField(
            model_name='voyageur',
            old_name='nom',
            new_name='numero_telephone',
        ),
        migrations.RemoveField(
            model_name='expediteur',
            name='age',
        ),
        migrations.RemoveField(
            model_name='expediteur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='expediteur',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='voyageur',
            name='age',
        ),
        migrations.RemoveField(
            model_name='voyageur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='voyageur',
            name='prenom',
        ),
        migrations.AddField(
            model_name='annonce',
            name='createur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ouanis.voyageur'),
        ),
        migrations.CreateModel(
            name='DemandeColis',
            fields=[
                ('demande_annonce', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ouanis.demandeannonce')),
                ('poids', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DemandeCourier',
            fields=[
                ('demande_annonce', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ouanis.demandeannonce')),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.AddField(
            model_name='demandeannonce',
            name='annonce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ouanis.annonce'),
        ),
        migrations.AddField(
            model_name='demandeannonce',
            name='destinataire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandes_destinataire', to='ouanis.voyageur'),
        ),
        migrations.AddField(
            model_name='demandeannonce',
            name='expediteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandes_expediteur', to='ouanis.expediteur'),
        ),
    ]
