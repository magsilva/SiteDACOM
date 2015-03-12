from tasks import processar
from models import CV
from django import forms

class CVForm(forms.ModelForm):
  class Meta:
    model = CV
    fields = ['lid', 'categoria']

def index(request):
  form = CVForm(request.POST or None)

  if form.is_valid():
    if not CV.objects.filter(lid=form.cleaned_data['lid'], categoria=form.cleaned_data['categoria']):
      objeto = form.save(commit=False)
      objeto.status = 1 #processando
      objeto.save()
      res = processar.delay(objeto.lid, objeto.categoria)
    #return redirect("http://site.ufsm.br/lattes/status/%s/%s/" % (form.cleaned_data['lid'], form.cleaned_data['categoria']))
    return redirect("status", lid=form.cleaned_data['lid'], categoria=form.cleaned_data['categoria'])

  return render(request, "index.html", {"form": form,})


def processando(request, lid=None, categoria=None):
  if lid:
    objeto = get_object_or_404(CV, lid=lid, categoria=categoria)
    return render(request, "status.html", {'objeto': objeto})

  return redirect("index")
