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
- Résolution d'écran :
  - Fonctionne avec toutes les résolutions (ajustement automatique)
  - Résolution recommandée : 1366x768 ou supérieure
- Configuration du navigateur :
  - Zoom à 100% (Ctrl + 0)
  - Mode plein écran (F11)
  - Échelle Windows à 100%

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/Enzzo-SF/rollercoin-bot.git
cd rollercoin-bot
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration

Modifiez le fichier `Routine_config.py` pour ajuster :
- Les positions des jeux sur votre écran
- Le niveau du jeu Memory
- La gestion de la bannière d'événement

## Utilisation

1. Connectez-vous à RollerCoin dans votre navigateur
2. Assurez-vous que :
   - La fenêtre du navigateur est en plein écran (F11)
   - Le zoom est à 100% (Ctrl + 0)
   - L'échelle Windows est à 100%
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

## Résolution des problèmes

Si le bot ne clique pas aux bons endroits :
1. Assurez-vous que le zoom du navigateur est à 100%
2. Activez le mode plein écran (F11)
3. Vérifiez l'échelle Windows (doit être à 100%)
4. Si les clics sont légèrement décalés, vous pouvez ajuster les coordonnées de base dans `Routine_config.py` :
   ```python
   _POSITION_BASE_COINCLICK = (1300, 420)  # Modifiez ces valeurs
   _POSITION_BASE_MEMORY = (600, 1000)     # si nécessaire
   _POSITION_BASE_JEU2048 = (1300, 850)    # pour votre écran
   ```

## Avertissement

Ce bot est fourni à des fins éducatives uniquement. L'utilisation de bots peut être contraire aux conditions d'utilisation de RollerCoin. Utilisez-le à vos propres risques.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à proposer une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
