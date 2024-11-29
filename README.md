# Bot RollerCoin

Bot automatisé pour jouer aux mini-jeux sur RollerCoin.

## Fonctionnalités

- Joue automatiquement aux jeux :
  - CoinClick
  - Memory
  - 2048
- Collecte automatique des récompenses
- Interface en français
- Configuration facile des positions des jeux

## Prérequis

- Python 3.7 ou plus récent
- Bibliothèques Python :
  - selenium
  - pyautogui
  - Pillow
  - numpy

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-nom/rollercoin-bot.git
cd rollercoin-bot
```

2. Installez les dépendances :
```bash
pip install selenium pyautogui Pillow numpy
```

## Configuration

Modifiez le fichier `Routine_config.py` pour ajuster :
- Les positions des jeux sur votre écran
- Le niveau du jeu Memory
- La gestion de la bannière d'événement

## Utilisation

1. Connectez-vous à RollerCoin dans votre navigateur
2. Assurez-vous que la fenêtre du navigateur est bien visible
3. Lancez le bot :
```bash
python Routine.py
```

Pour arrêter le bot, appuyez sur Ctrl+C dans le terminal.

## Structure du Projet

- `Routine.py` : Script principal du bot
- `Routine_config.py` : Configuration des positions et paramètres
- `functions.py` : Fonctions utilitaires et logique des jeux
- `2048Coins.py` : Logique du jeu 2048
- `CoinClick.py` : Logique du jeu CoinClick
- `HamsterClimber.py` : Logique du jeu Hamster Climber

## Avertissement

Ce bot est fourni à des fins éducatives uniquement. L'utilisation de bots peut être contraire aux conditions d'utilisation de RollerCoin. Utilisez-le à vos propres risques.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
