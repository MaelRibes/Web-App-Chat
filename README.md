# INFO834 - Web-App-Chat
Auteurs : BOUGHANMI Rami, HENRIQUES DOS SANTOS Joaquim, RIBES Maël, WALLERAND Alex

## Présentation

Pour ce projet, nous avons réaliser une application web de messagerie instantanée, qui fonctionne par salon. Les utilisateurs peuvent s'inscrire pour pouvoir converser en rejoignant des salons de discussion.

## Technologies utilisées

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/fr/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
[![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/fr-fr)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)

Nous avons décidé d'utiliser le framework Django Python pour le BackEnd serveur, qui communiquent avec le client par des views HTML, contenant du code JavaScript. En ce qui concerne les bases de données, nous utilisons MongoDB afin de stocker les données sur les salons et les messages qu'elles contiennent. Puis la base SQLite native à Django, pour les données des utilisateurs. Enfin, Redis permet de gérer la session utilisateur, enregistrer les historiques de connexion et est utilisé comme canal pour les sockets entre client et serveur.

## Installation

Le projet est déjà configuré pour fonctionner sur les adresses et ports classique de chacune des technologies utilisées. La base MongoDB est sur un cluster directement accessible, cependant il faut avoir un serveur Redis qui fonctionne en local.
Pour lancer le projet, il suffit de se placer dans la racine de ce répertoire et d'exécuter la commande suivante :
```
python manage.py runserver
```

## Organisation de l'équipe

En ce qui concerne la gestion de projet, nous avons répartis les tâches pour que chacun puissent apporter une fonctionnalité importante à l'application. Cette organisation est modélisée par les différentes branches du projet qui représentent chacune l'intégration d'une feature. Certaines on été faites en binôme, car relativement complexe. Globalement, nous avons tous fourni la même quantité de travail, c'est pourquoi nous décidons de nous attribuer à tous 25% de contribution au projet.

## Architecture de l'application

Django est un framework qui utilise le pattern MVC (Modèle-Vue-Contrôleur). L'application est donc décomposée avec les 3 éléments suivants : 
- Modèle : les objets de la DB Mongo (messages et salons)
- Vue : les pages HTML présentant les données
- Contrôleur : le code Python qui permet la logique des interactions de l'utilisateur avec le site


Il faut rajouter à ce modèle, la BD Redis, qui sert de cache pour la session des utilisateurs et de canal, pour pouvoir transmettre les messages de façon instantannée.

## Fonctionnalités développées

Nous avons implémenté toutes les fonctionnalités de bases de ce type d'application :
- Inscription et connexion
- Salon de discussion et messages
- Session utilisateur
- WebSocket pour les transmissions et réceptions instantanées

Premièrement, la création de compte et l'authentification sont gérés avec la base de données native de Django, SQLite. Nous avons choisi d'utiliser cette option plutôt que MongoDB, car elle simplifie grandement le processus d'authentification, ce qui nous a ainsi permis de nous concentrer sur d'autres fonctionnalités que nous n'avons auparavant jamais codé.

Ensuite, les données des salons sont enregistrées sur MongoDB avec les messages. Un salon est modélisé par son nom et son url. Un message possède les attributs suivants dans son schéma : auteur, contenu, date, salon. Le lien avec le salon est fait avec l'id unique généré par Mongo pour chaque objet salon, ce qui permet une recherche efficace du salon correspondant à un message. Les messages sont récupérées via une simple requête mongo qui collecte tous les messages du salon correspondant à la vue choisi par l'utilisateur, et envoyé à cette dernière afin de pouvoir les afficher.

Pour pouvoir affecter un utilisateur à un message, il faut que ses informations soit stockées dans une session. Pour cela, nous utilisons Redis qui va stocker les données dès lors qu'un utilisateur se connecte, et les supprimer lorsqu'il se déconnecte. Un middleware a été mis en place pour vérifier si un utilisateur est connecté pour pouvoir accéder aux salons de discussion.

Enfin, nous avons développé un système de canal entre le client et le serveur, grâce à des WebSocket et Redis. Lorsque le client se connecte à une vue d'un salon, un webscoket est initialisé. Lorsque le client envoie un message, le socket émet un événement contenant les données du message qui sera reçue du coté serveur, et mis en cache sur Redis, pour l'envoyer aux autres utilisateurs connectés sur le même salon. Ainsi, lorsque l'utilisateur appuie sur le bouton Envoyer, il s'excécute à la fois une requête POST pour enregistrer le message sur Mongo, et un événement socket pour envoyer le message instantanément aux autres clients.

## Compétences acquises

Nous avons utilisé le framework Django, car nous avons auparavant chacun déjà coder des projets utilisant JavaScipt pour le FrontEnd et le BackEnd. Cela nous ainsi permis d'apprendre le modèle MVC, qui est un standard aujourd'hui dans le développement web. De plus, nous avons ainsi pu remarquer que Django et Python sont des outils permettant de créer des applications robustes contrairement à ce que l'on pourrait croire, et que de nombreuses fonctionnalités natives du framework sont très utiles, comme la BD SQLite intégrée.

Ensuite, nous avons pu acquérir des compétences techniques sur les bases non relationnelles que sont Redis et MongoDB. Premièrement, nous avons pu voir que Mongo est une base "froide", qui permet de stocker rapidement des données de manière un peu brut, même s'il est toujours possible d'imposer un schéma à respecter. Puis Redis contrairement à Mongo, est une base "chaude", qui permet de récupérer rapidement de la donnée et peut être utilisé comme cache, notamment pour la session.

## Difficultés et améliorations possibles

Au cours de ce projet, nous avons rencontré quelques difficultés notamment lorsqu'il fallait fusionner les branches contenant les nouvelles fonctionnalités avec la branche main. Ceci du fait des conflits entre dossiers générés automatiquement au lancement de l'application, et du fichier contenant le code de la BD SQLite, qui est lui aussi constamment modifié à chaque utilisation. Une autre complexité rencontré pour chacun a été la compréhension du framework Django et du modèle MVC. Cependant, ce soucis s'est naturellement réglé au fil des commits et ajouts de features.

Le projet n'est pas complètement abouti, et de nombreuses fonctionnalités peuvent encore être implémentées. Tout d'abord, on pourrait rajouter des discussions privés entre 2 utilisateurs. Pour cela, il faudrait créer un autre objet discussion, qui prendrait les informations des deux utilisateurs souhaitant converser, et stocker leurs messages en faisant le lien avec ces derniers sur Mongo. Une autre fonctionnalité intéressante serait la possibilité d'ajouter des pièces jointes aux messages, notamment des images. Enfin, on pourrait ajouter une personnalisation complète du profil de chaque utilisateur, avec une photo, une description et des statistiques sur ses interactions avec l'application.