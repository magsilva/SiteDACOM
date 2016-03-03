import datetime
from haystack import indexes
from desenvolvimento.models import *


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    resumo = indexes.CharField(model_attr='resumo')
    datainicio = indexes.CharField(model_attr='Data Inicio')
    datadefim = indexes.CharField(model_attr='Data de Fim')
    agendafinanciadora = indexes.CharField(model_attr='Agencia Financiadora')
    situacao = indexes.CharField(model_attr='Situacao')
    natureza = indexes.CharField(model_attr='Natureza')
    professor = indexes.CharField()

    def prepare_tag_name(self, object):
        return object.professor.nome


    def get_model(self):
        return Projeto

    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter().all()