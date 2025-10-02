# Redis + FastAPI

## TODO list

Setup simple
- [x] Lancer un container Redis (ou Valkey) via Docker
- [x] Se connecter au serveur Redis et lancer la commande PING pour vérifier son bon fonctionnement

Prise en main et CRUD des String
- [x] ECRIRE des données dans la base
- [x] LIRE ses mêmes données
- [x] Modifier des données
- [x] Supprimer des données
- [x] Comment obtenir la liste des clés existantes ?
- [x] Comment vérifier si une une clé existe déjà ?

TTL
- [x] faire en sorte de donnée une durée de vie limitée à une donnée (TTL)
- [x] vérifier le temps restant avant que cette donnée ne soit supprimée  

Hash
- [x] découvrez ce que sont les Hash et réalisez un CRUD complet (exemple, un hash "user")
- [x] à quoi sert un Hash par rapport à une String ?

List
- [x] découvrez ce que sont les List et réalisez un CRUD complet (ajouter à la liste, retirer un élément etc) (liste de "commentaires")
- [x] à quoi sert une List ?

Set
- [x] découvrez ce que sont les Set et réalisez un CRUD (exemple: un set "categories")

ZSet
- [x] découvrez ce que sont les Zset et promis on arrete là !

Persistence
- [x] trouver comment activer la persistance sur Redis (AOF et/ou RDB)
- [x] pour tester, regarder si votre container contient bien un fichier de données sur le disque
- [x] enfin, trouver comment lancer un container Redis contenant DEJA des données issues d'une session précédente

Interface Graphique
- [x] Trouvez une image docker fournissant une interface graphique à Redis
- [x] Faites en sorte que l'interface graphique puisse se connecter à votre serveur afin de visualiser et manipuler les données qui s'y trouvent

Setup d'un vrai projet
- [x] créez un nouveau projet (document) qui vous servira de sandbox pour le reste des exercices
- [x] à la racine, créez un compose.yml (ou docker-compose.yml) dans lequel vous définirez un service "redis" (pensez à exposer le/les port(s))
- [x] OPTIONNEL: vous pouvez ajouter une interface graphique redis pour monitorer
- [x] mettez en place de la persistence et une configuration qui devra vivre dans un dossier `/docker/redis` par exemple (volume à monter)

Maitre et répliques
- [] en utilisant votre configuration actuelle, faite de votre service "redis" une instance maitresse et ajoutez 2 services "redis-r1", "redis-r2" qui doivent agir en répliques
- [] pour vérifier que tout fonctionne, écrivez des données, et essayez de les lire directement en vous connectant à une des instances "réplique"

Mise en place d'une API python avec FastAPI
- [] ajoutez au projet un dossier /app qui contiendra tout le code source de votre application python
- [] mettez en place un [venv](https://docs.python.org/3/library/venv.html) afin d'éviter d'installer les dépendences du projet globalement sur votre machine
- [] installez dans le venv FastAPI en suivant la [documentation officielle du framework](https://fastapi.tiangolo.com/)
- [] pour vérifiez que tout fonctionne, faites une simple route de test (genre "Hello world") et connectez y vous

CRUD des Articles
- [] définissez une class python "Article" (title, content...)
- [] route GET /article/{id} doit retourner l'article en question
- [] route POST /article doit créer un article grâce à un payload json (title, contenu)
- [] route DELETE /article/{id} supprime l'article à l'id donné
- [] route PATCH /article/{id} update l'article à l'article donné si il existe
- [] trouvez comment isoler toutes ces routes dans un fichier séparé (/routes/articles.py) et donnez le prefix "/article" à toutes ces routes (vous ferez de même avec les autres CRUD)

Pseudo-relations
- [] comment organiser son code si je veux commencer à tisser des relations entre mes models (Article, Comment, User...) ?
- [] admettons que mon Article est écrit par un User: comment faire, depuis l'id d'un article, pour récupérer les données de son auteur ?
- [] faire en sorte que l'on puisse récupérer les Categories d'un article (many-to-many ?)

Pokedex
- [] vous utiliserez l'api gratuite [pokeapi](https://pokeapi.co/)
- [] faites une plusieurs routes (prefix "/pokedex") qui doivent servir de proxy à la pokeapi afin de gagner en performance (ex: si votre user va sur la route /pokeapi/pokemon/ditto, il faudra lui renvoyer LE PLUS VITE POSSIBLE les informations concernant ce pokemon en interrogeant, ou pas, la pokeapi)
