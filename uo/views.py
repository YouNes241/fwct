from django.shortcuts import render, get_object_or_404 ,redirect
from uo.models import Formation, UE
from uo.forms import Ue_form

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout

def home(requete):
    return render(requete, 'accueil.html')

def a_propos(requete):
    return render(requete, 'a-propos.html')

def formations(requete):
    fs = Formation.objects.order_by('-intitule')
    return render(requete, 'formations.html', {'formations': fs})

def formation(requete, n):
    c = get_object_or_404(Formation, id=n)
    ue = UE.objects.filter(formations = c)
    permis = verif_ue_resp_formation(requete.user)
    return render(requete, 'formation.html', {'formation': c, 'ue': ue,'permis':permis})

def ue(requete, m):
    ue = get_object_or_404(UE, id=m)
    formations = Formation.objects.filter(ue__id = ue.id)
    permis = verif_ue_resp_formation(requete.user)
    return render(requete, 'ue.html', {'ue': ue, 'formations': formations , 'permis':permis})

def ues(requete):
    ues = UE.objects.order_by('-titre')
    permis = verif_ue_resp_formation(requete.user)
    return render(requete, 'ues.html', {'ues': ues , 'permis':permis})

def check_save(form, requete):
    if form.is_valid():
        val = form.save(commit=False)
        val.save()
    return val.id

@login_required
def ajout_ue(requete) :
    if requete.method == "POST" :
        form = Ue_form(requete.POST)
        if form.is_valid() :
            form = Ue_form(requete.POST)
            id = check_save(form,requete)
            return redirect("ue", m=id)
    else :
        form = Ue_form()
    return render(requete,'ue_form.html',{"page_service":"Ajouter UE",'form': form , "button":"Ajouter"})

@login_required
def modif_ue(requete, m):
    ue = get_object_or_404(UE, id = m)
    resps = list(ue.responsables.all())
    formations = ue.formations.all()
    for f in formations :
        resps.append(f.responsable)
    if requete.user not in resps : 
        return redirect("home")

    if requete.method == "POST":
        form = Ue_form(requete.POST, instance = ue)
        if form.is_valid():
            m = check_save(form, requete)
            return redirect("ue", m = m)
    else:
        form = Ue_form(instance = ue)
    return render(requete, 'ue_form.html', {"page_service":"Modifier UE", "form": form, "button":"Modifier"})

@login_required
def supprimer_ue(requete, m):
    ue = get_object_or_404(UE, pk = m)
    formations = ue.formations.all()
    resps = []
    for f in formations :
        resps.append(f.responsable)
    if requete.user not in resps : 
        return redirect("home")

    if requete.method == "POST":
        ue.delete()
        return redirect("ues")
    return render(requete, "suppr_ue.html", {"ue":ue})


def verif_ue_resp_formation(user):
    permis = []
    ues = UE.objects.order_by('-titre')
    for ue in ues :
        formations = ue.formations.all()
        resps = []
        for f in formations :
            resps.append(f.responsable)
        if user in resps :
            permis.append(ue.id)
    return permis 



def login(requete):
    return render(requete, "login.html")

def user_logout(requete):
    logout(requete)
    return redirect("home")