import datetime
from haystack import indexes
from desenvolvimento.models import *


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    resumo = indexes.CharField(model_attr='resumo')

    # pub_date = index

    def get_model(self):
        return Projeto

    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter().all()