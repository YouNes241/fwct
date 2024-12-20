# Framework Web 1 - CT3

Groupe :

* Ali Mohamad <ali.mohamad@etu.univ-orleans.fr>
* Lucas Paulo <lucas.paulo@etu.univ-orleans.fr>
* Nicolas Paul <nicolas.paul1@etu.univ-orleans.fr>
* Younes Ouaammou <younes.ouaammou@etu.univ-orleans.fr>

## Question 1

Commandes utilisées :

```shell
django-admin startproject ct
python manage.py startapp uo
python manage.py runserver 0.0.0.0:8080
```

## Question 2

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080
```

## Question 3

Commandes utilisées :

```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8080
```

**Note :** l'application d'administration de Django est déjà installé
à la création du projet Django dans la question 1.


## Question 4

Commandes utilisées :
```bash
python manage.py dumpdata > uo/fixtures/enseignant.json
python manage.py loaddata uo/fixtures/enseignant.json
python manage.py runserver 0.0.0.0:8080&
```

## Question 5

Commandes utilisées :

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080&
```

## Question 6

Commandes utilisées :

```shell
python manage.py dumpdata uo.Formation > uo/fixtures/formation.json
python manage.py loaddata uo/fixtures/formation.json
python manage.py runserver 0.0.0.0:8080
```

## Question 7

Commandes utilisées :

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```

## Question 8

Etant donné que les champs d'une UE doivent tous être non-`null`, et qu'il nous est demandé de rajouter des UEs sans spécifier le(s) responsable(s) pour cette question , nous avons rajouté un responsable par défaut. Pour valider ces modifications, il faut refaire les migrations et recharger la table User.

Les UEs ont été ajoutées via le pannel admin.

Commandes utilisées :

```shell
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata enseignant
python manage.py dumpdata uo.Ue > uo/fixtures/ue.json
python manage.py loaddata ue
python manage.py runserver 0.0.0.0:8080
```

## Question 9

Vu que la création de la vue et template des UE se fait à la question 10, pour cette question le lien des UE dans la page formation ne revoie vers rien.

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 10

J'ai aussi modifié le template de formation pour ajouter le lien vers les UE

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 11

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```


## Question 12

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 13

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 14

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 15

Commandes utilisées :
```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 16

Commandes utilisées :
```shell
python manage.py runserver 0.0.0.0:8080&
```

## Question 17

Commandes utilisées :

```shell
python manage.py runserver 0.0.0.0:8080&
```
## Question 18

Le mot de passe de tout les comptes est fwct@2425
ou plus rarement fwct@2524

Commandes utililsées :

```shell
python manage.py runserver 0.0.0.0:8080&
```