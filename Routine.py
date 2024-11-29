from functions import *
from Routine_config import ConfigurationRoutineJeu

class AutomationJeu:
    def __init__(self):
        print("[INFO] Initialisation du bot...")
        # Positions des jeux
        self.position_coinclick = ConfigurationRoutineJeu.POSITION_COINCLICK()
        self.position_memory = ConfigurationRoutineJeu.POSITION_MEMORY()
        self.position_jeu2048 = ConfigurationRoutineJeu.POSITION_JEU2048()
        self.banniere_evenement = ConfigurationRoutineJeu.BANNIERE_EVENEMENT
        self.niveau_memory = ConfigurationRoutineJeu.NIVEAU_MEMORY
        print("[INFO] Configuration chargée avec succès")
        
    def attendre_jeu_pret(self, position_jeu):
        """
        Attend que le jeu soit prêt, avec plusieurs tentatives
        """
        max_tentatives = 1
        print(f"[INFO] Vérification de l'état du jeu à la position {position_jeu}")
        
        for tentative in range(max_tentatives):
            try:
                print(f"[DEBUG] Tentative {tentative + 1}/{max_tentatives}")
                deplacer_souris(position_jeu[0], position_jeu[1])
                capture_avant = pyautogui.screenshot()
                print("[DEBUG] Capture d'écran avant le clic")
                
                clic(position_jeu[0], position_jeu[1])
                print(f"[DEBUG] Clic effectué à la position {position_jeu}")
                sleep(2)
                
                capture_apres = pyautogui.screenshot()
                print("[DEBUG] Capture d'écran après le clic")
                
                if not verifier_changement_avance(capture_avant, capture_apres):
                    print(f"[INFO] Jeu prêt à la tentative {tentative + 1}")
                    return True
                
            except Exception as e:
                print(f"[ERREUR] Erreur lors de la préparation du jeu : {str(e)}")
                print(f"[DEBUG] Détails de l'erreur : {type(e).__name__}")
            
            print(f"[INFO] Attente de 2 secondes avant la prochaine tentative")
            sleep(2)
        
        print("[AVERTISSEMENT] Impossible de préparer le jeu après toutes les tentatives")
        return False

    def jouer_memory(self):
        """
        Routine pour jouer à Memory
        """
        try:
            print("Démarrage du jeu Memory...")
            if not self.attendre_jeu_pret(self.position_memory):
                print("Impossible de démarrer Memory")
                return False
                
            clic(992, 500)  # Clic pour démarrer
            sleep(4)
            
            COORDONNEES_CELLULES = [
                [(850, 350), (1000, 350), (1150, 350)],
                [(850, 500), (1000, 500), (1150, 500)],
                [(850, 650), (1000, 650), (1150, 650)],
                [(850, 800), (1000, 800), (1150, 800)]
            ]
            
            COORDONNEES_CELLULES2 = [
                [(750, 350), (900, 350), (1050, 350), (1200, 350)],
                [(750, 500), (900, 500), (1050, 500), (1200, 500)],
                [(750, 650), (900, 650), (1050, 650), (1200, 650)]
            ]
            
            if self.niveau_memory == 1:
                memory_game = BotMemory(COORDONNEES_CELLULES)
            else:
                memory_game = BotMemory(COORDONNEES_CELLULES2)
                
            memory_game.jouer_partie()
            sleep(3)
            clic(967, 645)  # Gain de puissance
            sleep(3)
            return True
            
        except Exception as e:
            print(f"Erreur dans Memory : {e}")
            return False

    def jouer_coinclick(self):
        """
        Routine pour jouer à CoinClick
        """
        try:
            print("Démarrage du jeu CoinClick...")
            if not self.attendre_jeu_pret(self.position_coinclick):
                print("Impossible de démarrer CoinClick")
                return False
                
            clic(992, 438)  # Clic pour démarrer
            sleep(5)
            coinclick(1)
            sleep(3)
            clic(967, 645)  # Gain de puissance
            sleep(3)
            return True
            
        except Exception as e:
            print(f"Erreur dans CoinClick : {e}")
            return False

    def jouer_2048(self):
        """
        Routine pour jouer à 2048
        """
        try:
            print("Démarrage du jeu 2048...")
            if not self.attendre_jeu_pret(self.position_jeu2048):
                print("Impossible de démarrer 2048")
                return False
                
            clic(992, 504)  # Clic pour démarrer
            sleep(4)
            Jeu2048()
            sleep(3)
            clic(967, 645)  # Gain de puissance
            sleep(3)
            return True
            
        except Exception as e:
            print(f"Erreur dans 2048 : {e}")
            return False

    def lancer_automation(self):
        """
        Lance l'automatisation des jeux
        """
        print("Démarrage de l'automatisation des jeux...")
        clic(800, 150)
        sleep(1)
        pyautogui.scroll(500)
        
        if self.banniere_evenement:
            pyautogui.scroll(-300)
            
        while True:
            # Essai CoinClick
            if self.attendre_jeu_pret(self.position_coinclick):
                if self.jouer_coinclick():
                    pyautogui.press('f5')
                    sleep(15)
                    pyautogui.scroll(500)
                    if self.banniere_evenement:
                        pyautogui.scroll(-300)
                    continue

            # Essai Memory
            if self.attendre_jeu_pret(self.position_memory):
                if self.jouer_memory():
                    pyautogui.press('f5')
                    sleep(15)
                    pyautogui.scroll(500)
                    if self.banniere_evenement:
                        pyautogui.scroll(-300)
                    continue

            # Essai 2048
            if self.attendre_jeu_pret(self.position_jeu2048):
                if self.jouer_2048():
                    pyautogui.press('f5')
                    sleep(15)
                    pyautogui.scroll(500)
                    if self.banniere_evenement:
                        pyautogui.scroll(-300)
                    continue

            print("Aucun jeu disponible. Attente et réessai...")
            sleep(30)

if __name__ == "__main__":
    print("Démarrage du bot RollerCoin...")
    print("Assurez-vous que la fenêtre du navigateur est visible et que vous êtes connecté à RollerCoin")
    print("Appuyez sur Ctrl+C pour arrêter le bot")
    
    try:
        automation = AutomationJeu()
        automation.lancer_automation()
    except KeyboardInterrupt:
        print("\nArrêt du bot...")
    except Exception as e:
        print(f"Erreur inattendue : {e}")