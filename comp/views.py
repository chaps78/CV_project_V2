#from django.shortcuts import render
from django.http import HttpResponse
#from .models import COMPETENCES
from .models import Niveaux, Experiences, Competences, Contacts, Messages 
from django.template import loader
import os
from django.conf import settings
#from ./../CV_project/settings import LANGUE

from .forms import ContactForm
from django.shortcuts import render
# Create your views here.

#Recuperation de la langue du site pour la session
def get_langue(request):
    try:
        langue = request.session['langue']
    except:
        langue = 'en'
    return langue



def contact(request):
    if request.method == 'POST':
#        form = ContactForm(request.POST)
#        if form.is_valid():
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        message = request.POST.get('message')
#        else:
#            context['errors'] = form.errors.items()
        cont = Contacts.objects.filter(email=email)
        if not cont.exists():
            # If a contact is not registered, create a new one.
            cont = Contacts.objects.create(
                email=email,
                nom=nom,
                prenom=prenom
            )
        else:
            cont = cont.first()
        mess = Messages.objects.create(
                detail=message,
                contact=cont)
        context = {
            'nom' : nom,
            'email' : email
        }
        return render(request, 'comp/merci.html', context)
    else:
        form = ContactForm()
        lang = get_langue(request)
        context = {
            'langue' : lang,
            'form': form
        }
        return render(request, 'comp/contact.html', context)
#    lang = get_langue(request)
#    context = {
#        'langue' : lang
#        }
#    template = loader.get_template('comp/contact.html')
#    return HttpResponse(template.render(context, request=request))

def hobbies(request):
    lang = get_langue(request)
    context = {
        'langue' : lang
        }
    template = loader.get_template('comp/hobbies.html')
    return HttpResponse(template.render(context, request=request))


def fr(request):
    request.session['langue'] = 'fr'
    lang = get_langue(request)
    context = {
        'langue' : lang
        }
    template = loader.get_template('comp/home.html')
    return HttpResponse(template.render(context, request=request))

def en(request):
    request.session['langue'] = 'en'
    lang = get_langue(request)
    context = {
        'langue' : lang 
        }
    template = loader.get_template('comp/home.html')
    return HttpResponse(template.render(context,request=request))


def detail_comp(request,comp_id):
    

#    competences = Competences.objects.all()
#    context = {
#        'comp_id': competences
#    }
    message = "TOTO"
    return HttpResponse(message)

def competences(request,comp_id=0):
    os.system('echo "fr" >> toto.log')
    #settings.LANGUE=2
    competences = Competences.objects.all().order_by('niveau_id')
    niveaux = Niveaux.objects.all()
    template = loader.get_template('comp/competences.html')
    lang = get_langue(request)
    if comp_id==0:
        if lang == 'fr':
            intitule = "Cliquez sur une compétence pour avoir plus de détails."
        else:
            intitule = "Click here to get more details."
        context = {
            'langue' : lang ,
            'competences': competences,
            'niveaux' : niveaux,
            'intitule' : intitule
        }
    else:
        try:
            comp_select = Competences.objects.get(id=comp_id)
            lang = get_langue(request)
            if lang == 'fr':
                intitule = comp_select.detail
            else:
                intitule = comp_select.detail_en
            compet=comp_select.competence
        except:
            intitule = "Petit malin, tu crois que je ne t'ai pas vu???"
            compet=""
        context = {
            'langue' : lang ,
            'competences': competences ,
            'niveaux' : niveaux,
            'intitule' : intitule,
            'compet' : compet

        }

    return HttpResponse(template.render(context , request=request))

def experiences(request,xp_id=0):
    template = loader.get_template('comp/experiences.html')
    experiences = Experiences.objects.all().order_by('date_debut')
    lang = get_langue(request)
    for xp in experiences:
        xp.debut=xp.date_debut.strftime("%m/%Y")
        xp.fin=xp.date_fin.strftime("%m/%Y")

    if xp_id == 0:
        context = {
            'langue' : lang ,
            'experiences' : experiences,
            'xp_id' : xp_id
        }
    else:
        try:
            exp_select = Experiences.objects.get(id=xp_id)
            detail = exp_select
            detail.date_debut = detail.date_debut.strftime("%m/%Y")
            detail.date_fin = detail.date_fin.strftime("%m/%Y")
            compet = exp_select.compet.all()
        except:
            detail = "Petit malin tu crois que je ne t'ai pas vu???"
        context = {
            'langue' : lang ,
            'experiences' : experiences ,
            'detail' : detail,
            'compet' : compet,
            'xp_id' : xp_id
        }
    return HttpResponse(template.render(context , request=request))

def home(request):
    lang = get_langue(request)
    context = {
        'langue' : lang ,
        }
    template = loader.get_template('comp/home.html')
    return HttpResponse(template.render(context,request=request))


#def listing(request):
#    competences = ["<li>{}</li>".format(competence['comp']) for competence in COMPETENCES]
#    message = """<ul>{}</ul>""".format("\n".join(competences))
#    return HttpResponse(message)

#def detail(request, comp_id):
#    id = int(comp_id) # make sure we have an integer.
#    competence = COMPETENCES[id] # get the album with its id.
#    niveaux = " ".join([niveau['detail'] for niveau in competence['niveau']]) # grab artists name and create a string out of it.
#    message = "Pour la compétence suivante {}. Mon niveau est: {}".format(competence['comp'], niveaux)
#    return HttpResponse(message)


#def search(request):
#    query = request.GET.get('query')
#    if not query:
#        message = "Aucune compétence n'est demandé"
#    else:
#        competences = [
#            competence for competence in COMPETENCES
#            if query in " ".join(niveau['intitule'] for niveau in competence['niveau'])
#        ]
#
#        if len(competences) == 0:
#            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
#        else:
#            competences = ["<li>{}</li>".format(competence['comp']) for competence in competences]
#            message = """
#                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
#                <ul>
#                    {}
#                </ul>
#
#            """.format("".join(competences))
#   #         """.format("</li><li>".join(competences))
#
#    return HttpResponse(message)









