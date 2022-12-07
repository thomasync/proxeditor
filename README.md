# Proxeditor
### Proxy qui permet de supprimer les pubs et de modifier les requêtes des sites facilement

À la base j'avais crée ce proxy pour mes parents, je m'étais rendu compte que pour des personnes n'utilisant pas forcément beaucoup la technologie. Toutes les popups, demandes de cookies, d'authentification... Rendait l'usage d'une tablette très difficile ou même des sites en général.

Personnellement, j'ai mis en place ce proxy sur un raspberry local avec pas mal d'utilisations diverses :

- Avoir des applications en version premium
- Modifier les réponses de certains sites pour ajouter des balises *script* afin d'améliorer la navigation et par example automatiquement se connecter aux comptes, rediriger vers la bonne page, supprimer des éléments supperflus...
- Également, modifier les réponses des sites pour ajouter des balises *style* pour rendre les sites plus ergonomiques (augmenter les polices, darkmode, viewport...)

Afin de respecter les sites en question, je ne publierais pas les sites modifiés et le type de modification dans le répertoire **hosts/**.

Mais le fichier _example.py est assez explicite et simple à comprendre, c'est la base que j'utilise pour chaque site.

<br />

1. La commande pour lancer docker :
```
    docker compose up
    OU
    docker compose up -d // En background
```

⭐️ Le docker intègre les DNS de [AdGuard](https://adguard-dns.io/) pour supprimer toutes les pubs, même dans les applications

Ou alors le lancer directement :
```
pip install mitmproxy
pip install tldextract

chmod a+x proxy.sh
./proxy.sh
```

Les ports accessibles :
    
- Le proxy : **8302**
- L'interface en mode développement : **8301**

2. Se rendre dans les paramètres de son device et mettre l'ip du serveur ainsi que le port.

3. Se rendre sur http://mitm.it/ et récupérer le certificat

4. Ajouter le certificat dans les paramètres pour lui donner autorité.

- IOS : Réglages > Général > VPN et gestion de l'appareil > mitmproxy > Installer.

    - Réglages > Général > Informations > Réglages des certificats (tout en bas) > Cocher mitmproxy > Continuer.

- Android : Paramètres > Sécurité > Chiffrement et identifiants > Installer un certicat > Certificat CA > Installer quand même.

# Sécurité

1. Renommer le fichier *.env.example* -> *.env*
2. Passer l'*authentification=true* et modifier la valeur de *username* et *password*
```sh
authentification=true
username="thomas"
password="123456"
```


# Processus

1. Passer le proxy en mode ouvert (c'est à dire qu'il va tout intercepter au lieu de n'intercepter que les domaines définis)
```
// hosts/default.py:18

Remplacer 
data.ignore_connection = True

Par
data.ignore_connection = False
```

2. Copier le fichier **_example.py** dans le répertoire **hosts/**

3. Renommer la classe (Du même nom que le fichier pour s'y retrouver)

4. Pour le debug le process
    - Passer l'environnement en mode *production=false* dans le fichier *.env*
    - Se rendre sur l'interface http://127.0.0.1:8301
    - Et pour rendre ça encore plus agréable j'utlise [cette extension](https://chrome.google.com/webstore/detail/user-javascript-and-css/nbhcbdghjpllgmfilhnhkllmkecfmpld) 
    - Chargée avec ce script qui permet de recharger la page à chaque fois que le proxy redémarre (il est moche mais il marche)  :

```js
const ws = new WebSocket(`ws://${window.location.host}/updates`);
let inReload = false;

ws.addEventListener('open', () => {
    setTimeout(() => {
        document.querySelectorAll('.nav-tabs a')[2].click();
        setTimeout(() => {
            if(!document.querySelectorAll('.menu-content input')[3].checked) {
                document.querySelectorAll('.menu-content input')[3].click();   
                setTimeout(() => {
                    document.querySelectorAll('.eventlog .btn-primary').forEach((btn) => btn.click());
                    document.querySelectorAll('.eventlog .btn')[4].click();
                }, 10)
            }
        }, 10);
    }, 100);
});

ws.addEventListener('close', () => {
    setInterval(() => {
        new WebSocket(`ws://${window.location.host}/updates`).addEventListener('open', () => reload());
    }, 100);
});

const reload = () => {
    if(inReload) return;
    inReload = true;
    window.location.href = "http://" + window.location.host;
}
```


5. Envoyer des messages de sortie avec *logging.error()* depuis le proxy pour bien les discerner car la console défile trop vite

6. Ne pas oublier de refaire l'étape 1 dans le sens inverse sinon certains domaines sécurisés avec du SSL Pinning ne pourront pas charger

---

*Je ne suis pas responsable de l'utilisation de ce proxy. Ce proxy est uniquement à usage personnel pour mes parents. Ils sont seuls responsables de son utilisation et s'engagent à ne l'utiliser qu'à des fins légitimes et en conformité avec toutes les lois et réglementations applicables. Toute utilisation non autorisée ou illégale de ce proxy sera de votre seule responsabilité. Je décline toute responsabilité en ce qui concerne l'utilisation de ce proxy. Si vous avez des doutes sur l'utilisation légale de ce proxy, veuillez consulter un avocat qualifié.*