import pygame
import sys

# Farben definieren (RGB)
WHITE = (255, 255, 255)
# Füge hier die Pygame Initialisierung ein
pygame.init()
# Definiere Fenstergröße
WIDTH, HEIGHT = 300, 250
# Erstelle das Fenster und setze den Titel
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Taschenrechner")

# Hauptschleife
running = True
while running:
    
    # 1. Bildschirm füllen
    screen.fill(WHITE)
    # 2. Events verarbeiten (bei Aufgabe 11 nur QUIT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. Fenster aktualisieren - ab Aufgabe 12
    pass # Ersetze dies durch deinen Code

# Pygame beenden
# Füge hier den Code zum Beenden ein
pygame.quit()
sys.exit()