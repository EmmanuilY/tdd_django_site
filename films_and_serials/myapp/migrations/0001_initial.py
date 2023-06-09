# Generated by Django 4.2.1 on 2023-06-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Films",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Имя")),
                (
                    "url",
                    models.SlugField(
                        default=models.CharField(max_length=150, verbose_name="Имя"),
                        max_length=100,
                        unique=True,
                        verbose_name="url",
                    ),
                ),
                (
                    "poster",
                    models.ImageField(upload_to="posters/", verbose_name="Постер"),
                ),
                ("video", models.FileField(upload_to="video/", verbose_name="Видосик")),
                (
                    "subtitle",
                    models.FileField(
                        blank=True, upload_to="subtitle/", verbose_name="subtitle"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "film",
                "verbose_name_plural": "films",
            },
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.SmallIntegerField(verbose_name="Какой сезон")),
                (
                    "poster",
                    models.ImageField(upload_to="posters/", verbose_name="Постер"),
                ),
            ],
            options={
                "verbose_name": "season",
                "verbose_name_plural": "seasons",
            },
        ),
        migrations.CreateModel(
            name="Serial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Имя")),
                (
                    "url",
                    models.SlugField(
                        default=models.CharField(max_length=150, verbose_name="Имя"),
                        max_length=100,
                        unique=True,
                        verbose_name="url",
                    ),
                ),
                (
                    "poster",
                    models.ImageField(upload_to="posters/", verbose_name="Постер"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "serial",
                "verbose_name_plural": "serials",
            },
        ),
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.SmallIntegerField(verbose_name="Какая серия")),
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название серии"),
                ),
                (
                    "poster",
                    models.ImageField(upload_to="posters/", verbose_name="Постер"),
                ),
                ("video", models.FileField(upload_to="video/", verbose_name="Видосик")),
                (
                    "subtitle",
                    models.FileField(
                        blank=True, upload_to="subtitle/", verbose_name="subtitle"
                    ),
                ),
                (
                    "number_season",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.season",
                        verbose_name="Какой сезон",
                    ),
                ),
                (
                    "what_serial",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.serial",
                        verbose_name="Какой сериал",
                    ),
                ),
            ],
            options={
                "verbose_name": "seria",
                "verbose_name_plural": "series",
            },
        ),
        migrations.AddField(
            model_name="season",
            name="name_serial",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.serial",
                verbose_name="Какой сериал",
            ),
        ),
    ]
