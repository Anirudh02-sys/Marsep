# Generated by Django 4.1.2 on 2022-11-15 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcomepg', '0004_alter_user_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auditor', to=settings.AUTH_USER_MODEL)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contractor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]