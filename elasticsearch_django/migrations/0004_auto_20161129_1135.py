# Generated by Django 1.9 on 2016-11-29 11:35

from django.contrib.postgres.fields import JSONField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("elasticsearch_django", "0003_auto_20160926_2021")]

    operations = [
        # migrations.AlterField(
        #     model_name="searchquery",
        #     name="hits",
        #     field=JSONField(
        #         help_text="The list of meta info for each of the query matches returned."
        #     ),
        # ),
        # migrations.AlterField(
        #     model_name="searchquery",
        #     name="query",
        #     field=JSONField(help_text="The raw ElasticSearch DSL query."),
        # ),
    ]
