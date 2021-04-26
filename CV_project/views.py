#from django.shortcuts import render
from django.http import HttpResponse
#from .models import COMPETENCES
#from .models import Niveaux, Experiences, Competences
from django.template import loader

#LANGUE=1

# Create your views here.

def index(request):
#    message = "Salut tout le monde !"
#    return HttpResponse(message)
    template = loader.get_template('comp/index.html')
    return HttpResponse(template.render(request=request))
    # request albums
#    competences = Competences.objects.filter(niveau_id=2)[:12]
    # then format the request.
    # note that we don't use album['name'] anymore but album.name
    # because it's now an attribute.
#    formatted_competences = ["<li>{}</li>".format(competence.competence) for competence in competences]
#    message = """<ul>{}</ul>""".format("\n".join(formatted_competences))
#    return HttpResponse(message)



#def fr(request):
#    LANGUE=1

#def en(request):
#    LANGUE=2

