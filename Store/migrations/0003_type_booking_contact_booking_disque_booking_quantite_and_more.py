# Generated by Django 4.1.2 on 2022-11-13 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_artiste_chanson_disque_genre_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.contact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='disque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.disque'),
        ),
        migrations.AddField(
            model_name='booking',
            name='quantite',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='chanson',
            name='artistes',
            field=models.ManyToManyField(blank=True, related_name='chansons', to='Store.artiste'),
        ),
        migrations.AddField(
            model_name='chanson',
            name='disque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.disque'),
        ),
        migrations.AddField(
            model_name='disque',
            name='artistes',
            field=models.ManyToManyField(blank=True, related_name='disque', to='Store.artiste'),
        ),
        migrations.AddField(
            model_name='disque',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.genre'),
        ),
        migrations.AddField(
            model_name='disque',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.contact'),
        ),
        migrations.AddField(
            model_name='disque',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Store.type'),
        ),
    ]