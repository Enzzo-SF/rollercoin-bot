# Configuration de la routine de jeu
from functions import ajuster_coordonnees

class ConfigurationRoutineJeu:
    # Configuration de l'interface
    BANNIERE_EVENEMENT = True          # Ajustement pour la bannière d'événement
    NIVEAU_MEMORY = 1                  # Niveau du jeu Memory (1 ou 2)

    # Positions de base (pour 1920x1080)
    _POSITION_BASE_COINCLICK = (1300, 420)
    _POSITION_BASE_MEMORY = (600, 1000)
    _POSITION_BASE_JEU2048 = (1300, 850)
    
    @classmethod
    def POSITION_COINCLICK(cls):
        return ajuster_coordonnees(*cls._POSITION_BASE_COINCLICK)
    
    @classmethod
    def POSITION_MEMORY(cls):
        return ajuster_coordonnees(*cls._POSITION_BASE_MEMORY)
    
    @classmethod
    def POSITION_JEU2048(cls):
        return ajuster_coordonnees(*cls._POSITION_BASE_JEU2048)