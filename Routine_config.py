# Configuration de la routine de jeu
from functions import ajuster_coordonnees

class ConfigurationRoutineJeu:
    # Positions de base (pour 1920x1080)
    _POSITION_BASE_COINCLICK = (1300, 420)
    _POSITION_BASE_MEMORY = (600, 1000)
    _POSITION_BASE_JEU2048 = (1300, 850)
    
    @property
    def POSITION_COINCLICK(self):
        return ajuster_coordonnees(*self._POSITION_BASE_COINCLICK)
    
    @property
    def POSITION_MEMORY(self):
        return ajuster_coordonnees(*self._POSITION_BASE_MEMORY)
    
    @property
    def POSITION_JEU2048(self):
        return ajuster_coordonnees(*self._POSITION_BASE_JEU2048)
    
    # Configuration de l'interface
    BANNIERE_EVENEMENT = True          # Ajustement pour la bannière d'événement
    
    # Paramètres des jeux
    NIVEAU_MEMORY = 1                  # Niveau du jeu Memory (1 ou 2)