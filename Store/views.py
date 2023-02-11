from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .models import Banniere, Disque, Artiste
from django.core.paginator import Paginator


def index(request):
    # Récupération des cinq banières de la page 
    banieres = Banniere.objects.filter(nom__icontains = 'acceuil')[:5]
    # Récupération des disques valides
    disques = Disque.objects.filter(available=True)
    # Récupération des 12 nouvautés
    disques_new = disques.order_by('-parition')[:12]
    # Récupération des 12 tendances
    disques_trend = disques.order_by('-played')[:12]
    # Récupération des 12 favoris des utilisateurs
    disques_favorite = disques.order_by('-appreciation')[:12]
    banner_newsletter = Banniere.objects.get(nom = "banière newsletter")
    super_mixeur = Banniere.objects.get(nom = "banière super mixeur")
    
    context = {
        'banieres' : banieres,
        'disques_new' : disques_new,
        'disques_trend' : disques_trend,
        'disques_favorite' : disques_favorite,
        'banner_newsletter' : banner_newsletter,
        'super_mixeur' : super_mixeur,
    }
    return render(request, 'Store/index.html', context)


# def listing(request):
#     disques = Disque.objects.all()
#     formSearch = SearchForm()
#     context = {
#         "disques": disques,
#         'form': formSearch,
#     }
#     return render(request, 'Store/listing.html', context)

def listing(request):
    disques = Disque.objects.all().order_by("-id")
    paginator = Paginator(disques, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context ={
        "page_obj" : page_obj,
        "disques" : paginator
    }
    
    return render(request, 'Store/listing.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        disques = Disque.objects.all()
    else:
        disques = Disque.objects.filter(titre__icontains=query)
        if not disques.exists():
            disques = Disque.objects.filter(artistes__nom__icontains=query)
            if not disques.exists():
                disques = Disque.objects.filter(chanson__titre__icontains=query)
                if not disques.exists():
                    disques = Disque.objects.filter(genre__nom__iexact=query)
                    if not disques.exists():
                        disques = Disque.objects.filter(type__nom__iexact=query)
                        if not disques.exists():
                            disques = Disque.objects.filter(reference=query)
                            if not disques.exists():
                                disques = Disque.objects.filter(chanson__artistes__nom__icontains=query)
    if len(disques) == 0:
        disques_format = "Nous n'avons trouvé aucun disque!"
    elif len(disques) != 0:
        disques = ['<li>{}</li>'.format(disque.titre) for disque in disques]
        disques_format = "".join(disques)
        disques_format = "<ul>{}</ul>".format(disques_format)

    return HttpResponse(disques_format)


# def details(request, disque_id):
#     disque = Disque.objects.get(pk=disque_id)

#     context = {'disque': disque,}
#     return render(request, 'Store/details.html', context)

def details(request):
    bonjour = "Bonjour les gars !"
    context = {
        'bonjour' : bonjour,
    }
    return render(request, 'Store/details.html', context)
