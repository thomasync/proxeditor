# Changelog

## [0.0.3] - 2022-12-11

### Changed

- Déplacement de la logiqe de chargement des modules dynamiquement de __init__ vers proxy.py
- Remplacement de nodemon par nodemon-py-simple
- Remplacement de l'image docker nikolaik/python-nodejs par python:3.9-slim. Afin de prendre en charge les processeurs arm mais aussi optimiser le temps de build


## [0.0.2] - 2022-12-06

### Added

- Ajout des tests

### Changed

- Déplacement du répertoires des certificats dans .certs
- Ajout du fichier requirements.txt pour les dépendances python

## [0.0.1] - 2022-12-06

### Added

- Changelog.md pour garder les mises à jours
- .env afin d'avoir des variables plus globales
- Ajout de la possiblité de mettre une authentification

### Changed

- Changement du point d'entrée, docker-entrypoint.sh -> proxy.sh
