# Generated by Django 2.2.16 on 2020-09-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queuelength', '0003_auto_20200926_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='store_queue_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_id', models.CharField(max_length=255)),
                ('length', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]