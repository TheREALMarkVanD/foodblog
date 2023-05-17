# Generated by Django 4.2.1 on 2023-05-17 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_recipe_card_ingredients_delete_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]