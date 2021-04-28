from django.http import HttpResponse
from .models import Niveaux, Experiences, Competences, Contacts, Messages 
from django.template import loader
import os
from django.conf import settings

from .forms import ContactForm
from django.shortcuts import render
# Create your views here.

#Recuperation de la langue du site pour la session
def get_langue(request):
    try:
        langue = request.session['langue']
    except:
        #Si aucune langue n'est selectionné, par deffault c est en anglais
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



def competences(request,comp_id=0):
    os.system('echo "fr" >> toto.log')
    #settings.LANGUE=2
    competences = Competences.objects.all().order_by('niveau_id')
    niveaux = Niveaux.objects.all()
    template = loader.get_template('comp/competences.html')
    lang = get_langue(request)
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

    return HttpResponse(template.render(context , request=request))

def experiences(request,xp_id=0):
    template = loader.get_template('comp/experiences.html')
    experiences = Experiences.objects.all().order_by('date_debut')
    lang = get_langue(request)
    for xp in experiences:
        xp.debut=xp.date_debut.strftime("%m/%Y")
        xp.fin=xp.date_fin.strftime("%m/%Y")

    #Ajout des listes de competences aux experiences
    for exp in experiences:
        exp.comp = exp.compet.all() 

    context = {
        'langue' : lang ,
        'experiences' : experiences,
    }
    return HttpResponse(template.render(context , request=request))

def home(request):
    lang = get_langue(request)
    context = {
        'langue' : lang ,
        }
    template = loader.get_template('comp/home.html')
    return HttpResponse(template.render(context,request=request))



