# Generated by Django 3.2.16 on 2023-03-10 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('un_tran_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user_info_uid',
            field=models.ForeignKey(db_column='user_info_uid', on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='un_tran_report.userinfo'),
        ),
    ]