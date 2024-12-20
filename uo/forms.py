from django.forms import ModelForm
from uo.models import UE

class   Ue_form(ModelForm) :
    class Meta :
        model = UE
        fields = ["titre","description","horaires_cm","horaires_td","horaires_tp","ects","formations","responsables"]
        labels = {
        "titre":"Titre",
        "description":"Description",
        "horaires_cm":"Horaires CM",
        "horaires_td":"Horaires TD",
        "horaires_tp":"Horaires TP",
        "ects":"ECTS",
        "formations":"Formations",
        "responsables":"Responsables"
        }
