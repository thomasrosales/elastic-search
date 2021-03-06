from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer


"""
LOOKUP_FILTER_RANGE - to set the extent of your search,
LOOKUP_QUERY_GT - to search for the elements greater than the given value,
LOOKUP_QUERY_GTE - to search for the elements equal and greater than the given value,
LOOKUP_QUERY_LT - to search for the elements lesser than the given value,
LOOKUP_QUERY_LTE - to search for the elements equal and lesser than the given value. 
"""


class ArticleViewSet(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    # help us to search in all fields in one request,
    search_fields = (
        "title",
        "body",
    )

    # Filter fields
    # list which available fields to filter on
    filter_fields = {
        "id": {
            "field": "id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        "title": "title.raw",
        "body": "body.raw",
        "author": {
            "field": "author_pk",
            "lookups": [
                LOOKUP_QUERY_IN,
            ],
        },
        "created": "created",
        "modified": "modified",
        "pub_date": "pub_date",
    }

    # Define ordering fields
    # list which available fields to order on
    ordering_fields = {
        "id": "id",
        "title": "title.raw",
        "author": "author_id",
        "created": "created",
        "modified": "modified",
        "pub_date": "pub_date",
    }

    # Specify default ordering
    # you can set default order
    ordering = (
        "id",
        "created",
    )
