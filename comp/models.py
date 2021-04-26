#NIVEAU = {
#    'expert': {'intitule':'expert','detail':'peut prendre un sujet en autonomie et peut former un debutant','notation' : 4},
#    'confirme': {'intitule':'confirme','detail':'peut prendre le sujet en main avec besoin ponctuel de support','notation' : 3},
#    'debutant': {'intitule':'debutant','detail':'nécessite l\'accompagnement d\'un expert pour prendre le sujet en main','notation' : 2},
#    'notions': {'intitule':'notions','detail':'connaissance de l\'outil et des fonctionnalités qu\'il peut apporter','notation' : 1},
#}



#COMPETENCES = [
#    {'comp':'PYTHON','niveau':[NIVEAU['expert']]},
#    {'comp':'SQL','niveau':[NIVEAU['confirme']]},
#    {'comp':'MANAGEMENT','niveau':[NIVEAU['confirme']]},
#    {'comp':'shell','niveau':[NIVEAU['confirme']]},
#    {'comp':'wireshark','niveau':[NIVEAU['debutant']]},
#]



from django.db import models
from django.utils import timezone


class Niveaux(models.Model):
    niveau = models.CharField(max_length=200, unique=True)
    intitule = models.CharField(max_length=2000, unique=True)
    note = models.IntegerField(null=True)
    etoiles = models.CharField(max_length=50, unique=False, default='str')


class Competences(models.Model):
    competence = models.CharField(max_length=200, unique=True)
    #detail = models.CharField(max_length=2000, unique=True)
    detail = models.TextField(default=' ')
    detail_en = models.TextField(default=' ', unique=False)
    niveau = models.ForeignKey(Niveaux,on_delete=models.PROTECT)

class Experiences(models.Model):
    date_debut = models.DateTimeField(auto_now_add=False)
    date_fin = models.DateTimeField(auto_now_add=False)
    #date_fin.editable=True
    intitule = models.CharField(max_length=200, unique=False)
    intitule_en = models.CharField(max_length=200,default=' ', unique=False)
    client = models.CharField(max_length=200, unique=False)
    logo_client = models.CharField(max_length=200, unique=False)
    #detail = models.CharField(max_length=2000, unique=True)
    detail = models.TextField(default=' ')
    detail_en = models.TextField(default=' ')
    compet = models.ManyToManyField(Competences, related_name='experience', blank=True)



class Contacts(models.Model):
    nom = models.CharField(max_length=200, unique=False)
    prenom = models.CharField(max_length=200, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)



class Messages(models.Model):
    detail = models.TextField(default=' ',unique=False)
    contact = models.ForeignKey(Contacts,on_delete=models.PROTECT,null=True)
    created_at = models.DateTimeField(default=timezone.now)
#    created_at = models.DateTimeField(auto_now_add=True)

















