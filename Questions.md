1. Une route GET /stations crée une station. Quel verbe et quel code HTTP faut-il utiliser pour cette création ?

Il faut utiliser un code http:POST et le code de renvoie sera 201, pour confirmer que la création a bien eu lieu et que le post répond correctement 

2. GET /stations/999 demande une station inexistante. Quel code HTTP et quel type de réponse faut-il
renvoyer ?

"404 not found" et le mieux serai de renvoyer une réponse par json 

3. Quelle est la différence entre les codes 401 et 403 ? Donnez un exemple de chaque cas.

401 = authentification 
403 =  accès interdit, le serveur a bien recu la requete mais refuse  l'execution de la requete 

Exemple de code 401 : Nous essayons d'accéder à notre tableau de bord sur notre application web de getion de parking militaire sans être connecté. Le serveur me renvoie un 401 et me redirige vers une page de connexion.

Exemple de code 403 : Nous sommes connecté à un compte utilisateur standard sur un de gestion de parking de véhicule militaire, et nous essayons d'accéder à la page de gestion de carburant réseré aux administrateurs. Le serveur sait exactement qui je suis, mais il renvoie un 403 car notre rôle ne nous autorise pas à voir cette page.
