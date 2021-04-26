from django.contrib import admin

# Register your models here.

from .models import Niveaux,Competences,Experiences,Contacts,Messages


admin.site.register(Niveaux)
admin.site.register(Competences)
admin.site.register(Experiences)
admin.site.register(Contacts)
admin.site.register(Messages)

class ExperiencesAdmin(admin.ModelAdmin):
    readonly_fields = ('date_debut','date_fin')

#admin.site.register(Experiences,ExperiencesAdmin)


