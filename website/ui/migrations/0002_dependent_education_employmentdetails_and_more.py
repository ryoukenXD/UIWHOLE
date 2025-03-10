# Generated by Django 5.1.6 on 2025-03-10 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Elementary', 'Elementary'), ('High School', 'High School'), ('College', 'College'), ('Other', 'Other')], max_length=20)),
                ('school_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Contractual', 'Contractual'), ('Regular', 'Regular')], max_length=15)),
                ('date_hired', models.DateField()),
                ('latest_evaluation', models.DateField()),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sss', models.CharField(blank=True, max_length=20, null=True)),
                ('philhealth', models.CharField(blank=True, max_length=20, null=True)),
                ('pag_ibig', models.CharField(blank=True, max_length=20, null=True)),
                ('tin', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_type', models.CharField(choices=[('Mother', 'Mother'), ('Father', 'Father')], max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('birth_place', models.CharField(default='Unknown', max_length=255)),
                ('present_address', models.TextField()),
                ('provincial_address', models.TextField()),
                ('contact_number', models.CharField(max_length=20)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10)),
                ('spouse_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='parent',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='identification',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='employmentdetails',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='education',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='dependent',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.personnel'),
        ),
        migrations.AddField(
            model_name='employmentdetails',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ui.position'),
        ),
    ]
