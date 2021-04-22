# Generated by Django 3.0.7 on 2021-02-10 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0044_auto_20210207_1924"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="notification",
            name="notification_type_valid",
        ),
        migrations.AddField(
            model_name="notification",
            name="related_list_item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bookwyrm.ListItem",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("FAVORITE", "Favorite"),
                    ("REPLY", "Reply"),
                    ("MENTION", "Mention"),
                    ("TAG", "Tag"),
                    ("FOLLOW", "Follow"),
                    ("FOLLOW_REQUEST", "Follow Request"),
                    ("BOOST", "Boost"),
                    ("IMPORT", "Import"),
                    ("ADD", "Add"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="related_book",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bookwyrm.Edition",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="related_import",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bookwyrm.ImportJob",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="related_status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bookwyrm.Status",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="related_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name="notification",
            constraint=models.CheckConstraint(
                check=models.Q(
                    notification_type__in=[
                        "FAVORITE",
                        "REPLY",
                        "MENTION",
                        "TAG",
                        "FOLLOW",
                        "FOLLOW_REQUEST",
                        "BOOST",
                        "IMPORT",
                        "ADD",
                    ]
                ),
                name="notification_type_valid",
            ),
        ),
    ]
