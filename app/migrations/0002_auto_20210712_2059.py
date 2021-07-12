# Generated by Django 3.2.4 on 2021-07-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name'], 'verbose_name_plural': 'Languages'},
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56, unique=True)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.person')),
                ('projects', models.ManyToManyField(blank=True, to='app.Project')),
            ],
            options={
                'verbose_name_plural': 'Protocols',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='protocols',
            field=models.ManyToManyField(blank=True, to='app.Protocol'),
        ),
    ]
