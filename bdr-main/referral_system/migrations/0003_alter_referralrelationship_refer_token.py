# Generated by Django 4.0.1 on 2022-09-14 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referral_system', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referralrelationship',
            name='refer_token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral_code', to='referral_system.referralcode', verbose_name='referral_code'),
        ),
    ]
