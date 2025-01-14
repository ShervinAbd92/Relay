# Generated by Django 3.1.1 on 2020-09-10 19:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=64, verbose_name='relative path of actor')),
                ('remote', models.CharField(blank=True, max_length=500, verbose_name='remote reasoner resource')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=128, unique=True, verbose_name='agent unique name')),
                ('description', models.TextField(null=True, verbose_name='description of agent')),
                ('uri', models.URLField(max_length=256, verbose_name='base url of agent')),
                ('contact', models.EmailField(max_length=254, null=True)),
                ('registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=128, unique=True, verbose_name='channel name')),
                ('description', models.TextField(null=True, verbose_name='description of channel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.SlugField(verbose_name='Message name')),
                ('code', models.PositiveSmallIntegerField(default=200, verbose_name='HTTP status code')),
                ('status', models.CharField(choices=[('D', 'Done'), ('S', 'Stopped'), ('R', 'Running'), ('E', 'Error'), ('W', 'Waiting'), ('U', 'Unknown')], max_length=2)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('data', models.JSONField(null=True, verbose_name='data payload')),
                ('url', models.URLField(max_length=256, null=True, verbose_name='location of data')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tr_ars.actor')),
                ('ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tr_ars.message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='actor',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tr_ars.agent'),
        ),
        migrations.AddField(
            model_name='actor',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tr_ars.channel'),
        ),
        migrations.AddConstraint(
            model_name='actor',
            constraint=models.UniqueConstraint(fields=('channel', 'agent', 'path'), name='unique_actor'),
        ),
    ]
