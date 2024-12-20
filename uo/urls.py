from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('about/',            views.a_propos,   name = 'a_propos'),
    path('formation/',        views.formations, name='formations'),
    path('formation/<int:n>', views.formation,  name='formation'),
    path('ue/<int:m>',        views.ue,         name='ue'),
    path('ue/',               views.ues,        name='ues'),
    path('ue/ajouter',   views.ajout_ue, name='ajouter_ue'),
    path('ue/modifier/<int:m>', views.modif_ue, name="modif_ue"),
    path('ue/supprimer/<int:m>',views.supprimer_ue,name="suppr_ue"),
    path ("accounts/logout/",views.user_logout,name="logout"),
]
