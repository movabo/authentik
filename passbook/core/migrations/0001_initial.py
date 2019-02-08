# Generated by Django 2.1.5 on 2019-02-08 10:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


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
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('extra_data', models.TextField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='passbook_core.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expires', models.DateTimeField(blank=True, default=None, null=True)),
                ('fixed_username', models.TextField(blank=True, default=None)),
                ('fixed_email', models.TextField(blank=True, default=None)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invitation',
                'verbose_name_plural': 'Invitations',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('action', models.CharField(choices=[('allow', 'allow'), ('deny', 'deny')], max_length=20)),
                ('negate', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RuleModel',
            fields=[
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSourceConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('rulemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.RuleModel')),
                ('name', models.TextField()),
                ('slug', models.SlugField()),
                ('launch_url', models.URLField(blank=True, null=True)),
                ('icon_url', models.TextField(blank=True, null=True)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('provider', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='passbook_core.Provider')),
            ],
            options={
                'abstract': False,
            },
            bases=('passbook_core.rulemodel',),
        ),
        migrations.CreateModel(
            name='DebugRule',
            fields=[
                ('rule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.Rule')),
                ('result', models.BooleanField(default=False)),
                ('wait_min', models.IntegerField(default=5)),
                ('wait_max', models.IntegerField(default=30)),
            ],
            options={
                'verbose_name': 'Debug Rule',
                'verbose_name_plural': 'Debug Rules',
            },
            bases=('passbook_core.rule',),
        ),
        migrations.CreateModel(
            name='FieldMatcherRule',
            fields=[
                ('rule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.Rule')),
                ('user_field', models.TextField(choices=[('username', 'username'), ('first_name', 'first_name'), ('last_name', 'last_name'), ('email', 'email'), ('is_staff', 'is_staff'), ('is_active', 'is_active'), ('data_joined', 'data_joined')])),
                ('match_action', models.CharField(choices=[('startswith', 'Starts with'), ('endswith', 'Ends with'), ('endswith', 'Contains'), ('regexp', 'Regexp'), ('exact', 'Exact')], max_length=50)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Field matcher Rule',
                'verbose_name_plural': 'Field matcher Rules',
            },
            bases=('passbook_core.rule',),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('rulemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.RuleModel')),
                ('name', models.TextField()),
                ('slug', models.SlugField()),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('passbook_core.rulemodel',),
        ),
        migrations.CreateModel(
            name='WebhookRule',
            fields=[
                ('rule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='passbook_core.Rule')),
                ('url', models.URLField()),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE'), ('PUT', 'PUT')], max_length=10)),
                ('json_body', models.TextField()),
                ('json_headers', models.TextField()),
                ('result_jsonpath', models.TextField()),
                ('result_json_value', models.TextField()),
            ],
            options={
                'verbose_name': 'Webhook Rule',
                'verbose_name_plural': 'Webhook Rules',
            },
            bases=('passbook_core.rule',),
        ),
        migrations.AddField(
            model_name='rulemodel',
            name='rules',
            field=models.ManyToManyField(blank=True, to='passbook_core.Rule'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='passbook_core.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='usersourceconnection',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passbook_core.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'parent')},
        ),
        migrations.AddField(
            model_name='user',
            name='applications',
            field=models.ManyToManyField(to='passbook_core.Application'),
        ),
        migrations.AddField(
            model_name='user',
            name='sources',
            field=models.ManyToManyField(through='passbook_core.UserSourceConnection', to='passbook_core.Source'),
        ),
        migrations.AlterUniqueTogether(
            name='usersourceconnection',
            unique_together={('user', 'source')},
        ),
    ]
