import pygame
import sys

# Farben definieren (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
# Füge hier die Pygame Initialisierung ein
pygame.init()
# Definiere Fenstergröße
WIDTH, HEIGHT = 300, 250
# Erstelle das Fenster und setze den Titel
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Taschenrechner")
font = pygame.font.Font(None, 40)

equation = "0"
buttons = [
    ('/', 50, 100), ('*', 110, 100), ('-', 170, 100), ('+', 230, 100),
    ('=', 110, 160), ('C', 170, 160)
]
# Hauptschleife
running = True
while running:
    
    # 1. Bildschirm füllen
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (50, 30, 200, 40))
    equation_surface = font.render(equation, True, BLACK)
    screen.blit(equation_surface, (55, 40))#Für einen kleinen Abstand zum Rand
    for text, x, y in buttons:
        pygame.draw.rect(screen, GRAY, (x, y, 50, 50))
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (x + 15, y + 10))
    # 2. Events verarbeiten (bei Aufgabe 11 nur QUIT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. Fenster aktualisieren - ab Aufgabe 12
    pygame.display.flip()

# Pygame beenden
# Füge hier den Code zum Beenden ein
pygame.quit()
sys.exit()