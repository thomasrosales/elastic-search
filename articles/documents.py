from elasticsearch_dsl import analyzer, field

from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from .models import Article

# DOCUMENT ANALYZER

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)

# DOCUMENT DEFINITION


@registry.register_document
class ArticleDocument(Document):
    """Article Elasticsearch document."""

    class Index:
        # Name of the Elasticsearch index
        name = 'articles'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}


    author = fields.NestedField(properties={
        'pk': fields.IntegerField(),
    })
    

    class Django:
        model = Article
        fields = [
            "id",
            "title",
            "body",
            "created",
            "modified",
            "pub_date"
        ]
