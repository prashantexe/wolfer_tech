# Generated by Django 3.2.4 on 2023-02-14 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_auto_20230214_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeWork',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Sub_heading', models.CharField(max_length=200)),
                ('Point_1', models.CharField(max_length=200)),
                ('Point_2', models.CharField(max_length=200)),
                ('Point_3', models.CharField(max_length=200)),
                ('Point_4', models.CharField(max_length=200)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='HowWeWork/%Y/%m/%d')),
                ('last_updated_date', models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestordb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='angelinvestorsdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='awards',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='birac',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='centralgovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact_section',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='demodaydb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='events',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='eventsform',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='globalmarketconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='govt_tie',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='home_testimonial',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='international_partners',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='investors',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logo',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mbadb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorclinicdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mentorconnectdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mission',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='new_venturesdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ourstartup',
            name='image',
            field=models.ImageField(default='images/user_image.png', upload_to='OurStartup/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ourstartup',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sisfs',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stategovernmentfundingdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tbi',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonials',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='value',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venturecapitalistdb',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vision',
            name='last_updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 894329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='whoarewe',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 14, 16, 42, 56, 900799, tzinfo=utc)),
        ),
    ]