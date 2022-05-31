# Generated by Django 2.2.20 on 2021-05-11 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content_libraries', '0004_contentlibrary_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='LtiProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_id', models.CharField(help_text='The LTI platform identifier to which this profile belongs to.', max_length=255, verbose_name='platform identifier')),
                ('client_id', models.CharField(help_text='The LTI client identifier generated by the platform.', max_length=255, verbose_name='client identifier')),
                ('subject_id', models.CharField(help_text='Identifies the entity that initiated the deep linking request, commonly a user.  If set to ``None`` the profile belongs to the Anonymous entity.', max_length=255, verbose_name='subject identifier')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contentlibraries_lti_profile', to=settings.AUTH_USER_MODEL, verbose_name='open edx user')),
            ],
            options={
                'unique_together': {('platform_id', 'client_id', 'subject_id')},
            },
        ),
        migrations.CreateModel(
            name='LtiGradedResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_key', models.CharField(help_text='The usage key string of the blockstore resource serving the content of this launch.', max_length=255)),
                ('resource_id', models.CharField(help_text='The platform unique identifier of this resource in the platform, also known as "resource link id".', max_length=255)),
                ('resource_title', models.CharField(help_text='The platform descriptive title for this resource placed in the platform.', max_length=255, null=True)),
                ('ags_lineitem', models.CharField(help_text='If AGS was enabled during launch, this should hold the lineitem ID.', max_length=255)),
                ('profile', models.ForeignKey(help_text='The authorized LTI profile that launched the resource.', on_delete=django.db.models.deletion.CASCADE, related_name='lti_resources', to='content_libraries.LtiProfile')),
            ],
            options={
                'unique_together': {('usage_key', 'profile')},
            },
        ),
    ]