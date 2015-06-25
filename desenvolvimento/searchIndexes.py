__author__ = 'hgoncalves'
# import datetime
from haystack import indexes
from desenvolvimento.models import *


class ProjetoIndex(indexes.SearchIndex, indexes.Indexable):
    nameProjeto = indexes.CharField(document=True, use_template=True)
    # authorProjeto = indexes.CharField(model_attr='')
     # = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Projeto

    def index_queryset(self, using=Projeto):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(nome=using.nome)
