# Generated by Django 3.0.3 on 2020-02-19 06:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.contrib.postgres.fields import JSONField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
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
                ('private_key', models.TextField(blank=True, null=True)),
                ('public_key', models.TextField(blank=True, null=True)),
                ('actor', models.CharField(max_length=255, unique=True)),
                ('inbox', models.CharField(max_length=255, unique=True)),
                ('shared_inbox', models.CharField(blank=True, max_length=255, null=True)),
                ('outbox', models.CharField(max_length=255, unique=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('local', models.BooleanField(default=True)),
                ('fedireads_user', models.BooleanField(default=True)),
                ('localname', models.CharField(max_length=255, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('openlibrary_key', models.CharField(max_length=255)),
                ('data', JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('openlibrary_key', models.CharField(max_length=255, unique=True)),
                ('data', JSONField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('authors', models.ManyToManyField(to='bookwyrm.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FederatedServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('server_name', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(default='federated', max_length=255)),
                ('application_type', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=100)),
                ('editable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status_type', models.CharField(default='Note', max_length=255)),
                ('activity_type', models.CharField(default='Note', max_length=255)),
                ('local', models.BooleanField(default=True)),
                ('privacy', models.CharField(default='public', max_length=255)),
                ('sensitive', models.BooleanField(default=False)),
                ('mention_books', models.ManyToManyField(related_name='mention_book', to='bookwyrm.Book')),
                ('mention_users', models.ManyToManyField(related_name='mention_user', to=settings.AUTH_USER_MODEL)),
                ('reply_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='follows', max_length=100, null=True)),
                ('relationship_id', models.CharField(max_length=100)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_object', to=settings.AUTH_USER_MODEL)),
                ('user_subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_subject', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShelfBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Book')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Shelf')),
            ],
            options={
                'unique_together': {('book', 'shelf')},
            },
        ),
        migrations.AddField(
            model_name='shelf',
            name='books',
            field=models.ManyToManyField(through='bookwyrm.ShelfBook', to='bookwyrm.Book'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='shelves',
            field=models.ManyToManyField(through='bookwyrm.ShelfBook', to='bookwyrm.Shelf'),
        ),
        migrations.AddField(
            model_name='user',
            name='federated_server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.FederatedServer'),
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(through='bookwyrm.UserRelationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='shelf',
            unique_together={('user', 'identifier')},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('status_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookwyrm.Status')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Book')),
            ],
            options={
                'abstract': False,
            },
            bases=('bookwyrm.status',),
        ),
    ]
