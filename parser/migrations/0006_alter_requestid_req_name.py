# Generated by Django 5.1.1 on 2024-10-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0005_alter_requestid_req_id_alter_requestid_req_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestid',
            name='req_name',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
    ]
