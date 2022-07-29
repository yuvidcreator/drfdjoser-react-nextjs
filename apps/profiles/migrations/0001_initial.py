# Generated by Django 3.2.9 on 2022-07-29 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', upload_to='profiles/profile_pics', verbose_name='Profile Image')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='--', max_length=20, verbose_name='Gender')),
                ('address_line_1', models.CharField(blank=True, max_length=255, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=255, verbose_name='Address Line 2')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip Code')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('country', models.CharField(blank=True, default='India', max_length=255, verbose_name='Country')),
                ('about_me', models.TextField(blank=True, verbose_name='About Me')),
                ('is_mobile_verified', models.BooleanField(default=False, verbose_name='Mobile verified')),
                ('is_verified_customer', models.BooleanField(default=False, verbose_name='Customer verified')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin User')),
                ('is_manager', models.BooleanField(default=False, verbose_name='Store Manager User')),
                ('is_customer', models.BooleanField(default=False, verbose_name='Customer User')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
