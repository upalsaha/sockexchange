# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_email', models.EmailField(max_length=254)),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField(max_length=255)),
                ('review_title', models.CharField(max_length=30)),
                ('date_published', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('style', models.CharField(max_length=30)),
                ('theme', models.CharField(max_length=30)),
                ('seller', models.EmailField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='sock_reviewed',
            field=models.ForeignKey(to='SockExchange.Sock'),
        ),
        migrations.AddField(
            model_name='order',
            name='socks',
            field=models.ManyToManyField(to='SockExchange.Sock'),
        ),
    ]
