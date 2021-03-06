# Generated by Django 2.1.7 on 2019-05-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel_number', models.CharField(blank=True, max_length=15)),
                ('mail', models.EmailField(blank=True, max_length=5000)),
                ('regddate', models.DateField(blank=True)),
                ('status', models.IntegerField(choices=[('アクティブ', 'アクティブ'), ('非アクティブ', '非アクティブ'), ('優良', '優良'), ('取引終了', '取引終了'), ('運営者', '運営者')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel_number', models.CharField(blank=True, max_length=15)),
                ('mail', models.EmailField(blank=True, max_length=50)),
                ('regddate', models.DateField(blank=True)),
                ('status', models.IntegerField(choices=[('アクティブ', 'アクティブ'), ('非アクティブ', '非アクティブ'), ('優良', '優良'), ('利用終了', '利用終了'), ('運営者', '運営者')])),
            ],
        ),
    ]
