# Generated by Django 4.2.3 on 2023-09-09 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dietapp', '0004_pprofile_bmi_user_pfimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dietsuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(choices=[('0', 'Select Year'), ('8-15', 'children'), ('15-31', 'young age'), ('32-55', 'middle age'), ('55-above', 'post middle age')], default='0', max_length=9)),
                ('bmi', models.CharField(choices=[('<25', 'underweight'), ('>25', 'overweight'), ('=25', 'Healthyweight')], default='0', max_length=9)),
                ('subject', models.CharField(max_length=50)),
                ('descnote', models.CharField(max_length=10)),
                ('ntfle', models.FileField(upload_to='DataFiles')),
                ('date_created', models.DateField(auto_now=True)),
                ('sckey', models.CharField(max_length=10)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
