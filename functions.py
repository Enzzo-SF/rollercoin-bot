import pyautogui
from time import sleep
import numpy as np
from PIL import ImageGrab
from PIL import ImageChops
from typing import List, Tuple
import random
import time

# VARIABLES
bas = 'down'
haut = 'up'
droite = 'right'
gauche = 'left'
url = 'https://rollercoin.com/game/choose_game'

# PYAUTOGUI
def fleche(direction):
    pyautogui.press(direction)
    
def clic(position_x, position_y):
    pyautogui.click(position_x, position_y)

def deplacer_souris(position_x, position_y):
    pyautogui.moveTo(position_x, position_y)
    
def double_clic(position_x, position_y):
    pyautogui.doubleClick(position_x, position_y)

def clic_droit(position_x, position_y):
    pyautogui.rightClick(position_x, position_y)

def double_clic_droit(position_x, position_y):
    pyautogui.rightClick(position_x, position_y)

def glisser(position_x, position_y):
    pyautogui.dragTo(position_x, position_y)

def glisser_droit(position_x, position_y):
    pyautogui.dragTo(position_x, position_y, button='right')
    
def glisser_droit_double(position_x, position_y):
    pyautogui.dragTo(position_x, position_y, button='right', duration=2)

# Fonctions
def chercher_position():
    print('Positionnez le curseur...')
    sleep(3)
    print(pyautogui.position())
    key = input("Écrivez 'stop' pour arrêter, ou appuyez sur Entrée pour continuer...")
    return key

def similarite_image(image1, image2):
    diff = ImageChops.difference(image1, image2)
    diff = diff.convert('L')  # Conversion en niveaux de gris
    histogram = diff.histogram()
    rms = sum((value * ((idx % 256) ** 2) for idx, value in enumerate(histogram))) / float(image1.size[0] * image1.size[1])
    return rms ** 0.5

def verifier_changement(capture_avant, capture_apres):
    # Compare les deux images
    if ImageChops.difference(capture_avant, capture_apres).getbbox() is None:
        print("Les images sont identiques, l'action n'a pas causé de changements.")
        return True
    else:
        print("Les images sont différentes, l'action a causé des changements.")
        return False

def verifier_changement_avance(capture_avant, capture_apres):
    similarite = similarite_image(capture_avant, capture_apres)
    print("Similarité : ", similarite)
    
    if similarite > 6:
        print("Les images sont différentes, l'action a causé des changements significatifs.")
        return False
    else:
        print("Les images sont similaires, l'action a causé des changements minimes ou négligeables.")
        return True

def capturer_ecran_jeu():
    # Capture une image de la zone de jeu
    capture = ImageGrab.grab()
    capture_np = np.array(capture)
    return capture_np

#JEUX
def Jeu2048():
    #Variables
    attente = 0.1
    secondes = 0
   
    while secondes < 64:
        secondes += 1
        print(f"Seconde {secondes}")
        fleche(bas)
        sleep(attente)
        fleche(gauche)
        sleep(attente)
        fleche(bas)
        sleep(attente)
        fleche(droite)
        sleep(attente)               
        fleche(bas)

    print("Fin du jeu!")

def clic_souris(x, y, attente=0.2):
    pyautogui.click(x, y)
    sleep(attente)

def coinclick(a):
    print("DÉBUT DU JEU")
    while a==1:
        capture = pyautogui.screenshot(region=(530, 430, 828, 417))
        largeur, hauteur = capture.size
        for x in range(0, largeur, 5):
            for y in range(0, hauteur, 5):
                r, g, b = capture.getpixel((x, y))

                #Fin
                if b == 228 and r == 3 and g == 225:
                    a = 0
                    break

                 # Pièce ETH
                if b == 207 and r == 66 and g==105:
                    clic_souris(x + 535, y + 440, attente=0)
                    break

                # Pièce bleue
                if b == 183 and r == 0:
                    clic_souris(x + 530, y + 440, attente=0)
                    break

                # Pièce jaune
                if b == 64 and r == 200:
                    clic_souris(x + 530, y + 440, attente=0)
                    break

                # Pièce orange
                if b == 33 and r == 231:
                    clic_souris(x + 530, y + 440, attente=0)
                    break

                # Pièce grise
                if b == 230 and r == 230:
                    clic_souris(x + 535, y + 440, attente=0)
                    break
                
    print("FIN DU JEU")

class BotMemory:
    def __init__(self, coordonnees_cellules: List[List[Tuple[int, int]]]):
        self.coordonnees_cellules = coordonnees_cellules
        self.paires_trouvees = set()  # Garde une trace des paires déjà trouvées
        self.memoire_cartes = {}  # Dictionnaire pour mémoriser les couleurs des cartes {(ligne, colonne): couleur}
        
    def obtenir_couleur_carte(self, x: int, y: int) -> tuple:
        """Capture et renvoie la couleur dominante de la carte à la position spécifiée."""
        # Définit une zone de 20x20 pixels autour du point central de la carte
        region = (x-10, y-10, x+10, y+10)
        capture = ImageGrab.grab(bbox=region)
        
        # Convertit l'image en tableau numpy et calcule la couleur moyenne
        tableau_img = np.array(capture)
        couleur_moyenne = tuple(np.mean(tableau_img, axis=(0, 1)).astype(int))
        
        return couleur_moyenne
    
    def cartes_identiques(self, couleur1: tuple, couleur2: tuple) -> bool:
        """Compare deux couleurs pour déterminer si les cartes sont identiques."""
        # Calcule la différence entre les couleurs
        difference = sum(abs(a - b) for a, b in zip(couleur1, couleur2))
        print(f"Différence de couleur : {difference}")
        # Si la différence est inférieure à un seuil, considère les cartes comme identiques
        return difference < 50  # Vous pouvez ajuster ce seuil selon vos besoins
        
    def cliquer_et_obtenir_couleur(self, ligne: int, colonne: int) -> tuple:
        """Clique sur une carte et obtient sa couleur."""
        x, y = self.coordonnees_cellules[ligne][colonne]
        pyautogui.click(x, y)
        sleep(0.5)  # Attend que la carte se retourne
        return self.obtenir_couleur_carte(x, y)

    def obtenir_coups_disponibles(self) -> List[Tuple[int, int]]:
        """Renvoie toutes les cellules disponibles non encore appariées."""
        coups = []
        for ligne in range(len(self.coordonnees_cellules)):
            for colonne in range(len(self.coordonnees_cellules[ligne])):
                if (ligne, colonne) not in self.paires_trouvees:
                    coups.append((ligne, colonne))
        return coups
    
    def jouer_tour(self):
        """Exécute un tour de jeu."""
        coups_disponibles = self.obtenir_coups_disponibles()
        
        if len(coups_disponibles) < 2:
            return False  # Jeu terminé
            
        # Choisit la première carte à retourner
        premier_coup = random.choice(coups_disponibles)
        premiere_couleur = self.cliquer_et_obtenir_couleur(*premier_coup)
        
        # Retire le premier coup des coups disponibles
        coups_disponibles.remove(premier_coup)
        
        # Choisit la deuxième carte
        deuxieme_coup = random.choice(coups_disponibles)
        deuxieme_couleur = self.cliquer_et_obtenir_couleur(*deuxieme_coup)
        
        # Vérifie si les cartes correspondent
        if self.cartes_identiques(premiere_couleur, deuxieme_couleur):
            print("Paire trouvée !")
            self.paires_trouvees.add(premier_coup)
            self.paires_trouvees.add(deuxieme_coup)
        else:
            print("Pas de correspondance")
        
        return True
    
    def jouer_partie(self):
        """Joue une partie complète de Memory."""
        print("Début de la partie de Memory")
        while self.jouer_tour():
            sleep(1)  # Pause entre les tours
        print("Partie terminée !")

def obtenir_resolution():
    """Obtient la résolution actuelle de l'écran."""
    import pyautogui
    largeur, hauteur = pyautogui.size()
    return largeur, hauteur

def ajuster_coordonnees(x, y, resolution_base=(1920, 1080)):
    """Ajuste les coordonnées en fonction de la résolution actuelle."""
    largeur_actuelle, hauteur_actuelle = obtenir_resolution()
    ratio_x = largeur_actuelle / resolution_base[0]
    ratio_y = hauteur_actuelle / resolution_base[1]
    
    return (int(x * ratio_x), int(y * ratio_y))
