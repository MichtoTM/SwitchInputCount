import keyboard
import mouse
import time
import os

# Chemin absolu vers count.txt
file_path = os.path.join(os.path.dirname(__file__), 'count.txt')

def Save():
    KeyCountVars_hex = {key: hex(value) for key, value in KeyCountVars.items()}
    try:
        with open(file_path, 'w') as fichier:
            for key, value in KeyCountVars_hex.items():
                fichier.write(f"{key}: {value}\n")
    except PermissionError:
        print(f"Erreur de permission : impossible d'écrire dans {file_path}")

KeyCountVars = {}

def LoadSave():
    global KeyCountVars
    try:
        with open(file_path, 'r') as fichier:
            for ligne in fichier:
                partie = ligne.strip().split(': ')
                if len(partie) == 2:
                    key, value_hex = partie
                    value = int(value_hex, 16)
                    KeyCountVars[key] = value
        print("Chargement du fichier de sauvegarde réussi.")
    except FileNotFoundError:
        print(f"Le fichier de sauvegarde {file_path} n'existe pas.")
    except PermissionError:
        print(f"Erreur de permission : impossible de lire dans {file_path}")

def KeyCount(e):
    if isinstance(e, keyboard.KeyboardEvent):
        if e.event_type == keyboard.KEY_UP:
            key_name = e.name.lower()
            if key_name not in KeyCountVars:
                KeyCountVars[key_name] = 0
            KeyCountVars[key_name] += 1
            print(f"Vous avez appuyé sur {key_name.capitalize()} {KeyCountVars[key_name]} fois.")
    elif isinstance(e, mouse.ButtonEvent):
        if e.event_type == mouse.UP:
            button_name = None
            if e.button == mouse.LEFT:
                button_name = "Left Click"
            elif e.button == mouse.RIGHT:
                button_name = "Right Click"
            elif e.button == mouse.MIDDLE:
                button_name = "Wheel CLick"
            elif e.button == mouse.X2:
                button_name = "Side Front CLick"
            elif e.button == mouse.X:
                button_name = "Side Back CLick"
            elif e.button == mouse.X and e.event_type == mouse.UP:
                if e.button == 0:
                    button_name = "Side Back Button"
                elif e.button == 1:
                    button_name = "Side Front Button"
            if button_name:
                if button_name not in KeyCountVars:
                    KeyCountVars[button_name] = 0
                KeyCountVars[button_name] += 1
                print(f"Vous avez effectué un {button_name} {KeyCountVars[button_name]} fois.")
    elif isinstance(e, mouse.WheelEvent):
        wheel_name = "Front Wheel" if e.delta > 0 else "Back Wheel"
        if wheel_name not in KeyCountVars:
            KeyCountVars[wheel_name] = 0
        KeyCountVars[wheel_name] += 1
        print(f"Vous avez effectué une rotation {wheel_name} {KeyCountVars[wheel_name]} fois.")
    Save()

try:
    LoadSave()
except Exception as e:
    print(f"Erreur lors du chargement du fichier de sauvegarde: {e}")

keyboard.hook(KeyCount)
mouse.hook(KeyCount)

print("Appuyez sur une touche ou cliquez avec la souris pour compter les actions (Ctrl+C pour quitter) :")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()
    mouse.unhook_all()
    Save()