# Framework Web 1 - Devoir de contrôle terminal

Groupe :

* Ali Mohamad <ali.mohamad@etu.univ-orleans.fr>
* Lucas Paulo <lucas.paulo@etu.univ-orleans.fr>
* Nicolas Paul <nicolas.paul1@etu.univ-orleans.fr>
* Younes Ouaammou <younes.ouaammou@etu.univ-orleans.fr>

## Question 1

Commandes utilisées :

```bash
django-admin startproject ct
python manage.py startapp uo
python manage.py runserver 0.0.0.0:8080&
```

## Question 2 

Nous avons choisi d'implémenter une template de base dont les autres templates hériteront. La template de base sera complétée à la question 14.

Commandes utilisées : 

```bash
python manage.py runserver 0.0.0.0:8080&
```

## Question 3
L'application d'administration Django est déjà disponible à la création du projet.

Commandes utilisées :
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8080&
```


## Question 4

Commandes utilisées :
```bash
python manage.py dumpdata > uo/fixtures/enseignant.json
python manage.py loaddata uo/fixtures/enseignant.json
python manage.py runserver 0.0.0.0:8080&
```

