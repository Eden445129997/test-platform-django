# Generated by Django 3.0.6 on 2020-11-12 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b',
            name='a',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='qa_platform.A'),
        ),
    ]
