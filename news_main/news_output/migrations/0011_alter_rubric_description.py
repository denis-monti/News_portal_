# Generated by Django 4.1.4 on 2023-01-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_output', '0010_pgsroomreserving_rubric_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='description',
            field=models.TextField(error_messages={'null': 'Поле не заполнено'}, max_length=100, null=True, verbose_name='Описание рубрики'),
        ),
    ]
