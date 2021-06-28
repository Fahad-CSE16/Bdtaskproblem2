# Generated by Django 3.1.7 on 2021-06-28 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0005_auto_20210628_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='Aboss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='abosscomission', to='useraccounts.sellerprofile'),
        ),
        migrations.AddField(
            model_name='sell',
            name='Bboss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bbosscomission', to='useraccounts.sellerprofile'),
        ),
        migrations.AddField(
            model_name='sell',
            name='Cboss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cbosscomission', to='useraccounts.sellerprofile'),
        ),
        migrations.AddField(
            model_name='sell',
            name='Dboss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dbosscomission', to='useraccounts.sellerprofile'),
        ),
    ]
