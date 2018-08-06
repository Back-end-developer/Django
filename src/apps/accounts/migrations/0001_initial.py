# Generated by Django 2.0.2 on 2018-08-06 10:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, help_text='Обязательное поле. Не более 30 символов. Только буквы, цифры и символы @/./+/-/_.', max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='имя пользователя')),
                ('first_name', models.CharField(max_length=30, verbose_name='имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='middle name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='E-mail')),
                ('phone_number', models.CharField(blank=True, max_length=255, verbose_name='phone number')),
                ('is_staff', models.BooleanField(default=False, help_text='Отметьте, если пользователь может входить в административную часть сайта.', verbose_name='user status')),
                ('is_active', models.BooleanField(default=False, help_text='Отметьте, если пользователь должен считаться активным. Уберите эту отметку вместо удаления учётной записи.', verbose_name='Активный')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='registration date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]