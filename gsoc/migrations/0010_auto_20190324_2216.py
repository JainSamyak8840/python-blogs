# Generated by Django 2.1.7 on 2019-03-24 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsoc', '0009_reglink'),
    ]

    operations = [
        migrations.AddField(
            model_name='reglink',
            name='user_gsoc_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gsoc.GsocYear'),
        ),
        migrations.AddField(
            model_name='reglink',
            name='user_role',
            field=models.IntegerField(choices=[(0, 'Others'), (1, 'Suborg Admin'), (2, 'Mentor'), (3, 'Student')], default=0, null=True),
        ),
        migrations.AddField(
            model_name='reglink',
            name='user_suborg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gsoc.SubOrg'),
        ),
    ]