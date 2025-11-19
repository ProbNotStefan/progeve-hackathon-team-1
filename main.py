import pygame
import stats

player_cards = []
enemy_cards = []

def draw_card(screen, position, id):
    card_color = (255, 255, 255)
    card_rect = pygame.Rect(position[0], position[1], 100, 150)
    pygame.draw.rect(screen, card_color, card_rect)
    

def draw_all__cards(screen):
    for idx, id in enumerate(player_cards):
        draw_card(screen, (50 + idx * 110, 400), id)
    for idx, id in enumerate(enemy_cards):
        draw_card(screen, (50 + idx * 110, 50), id)

def get_card(id):




def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cards of Cuthulhu")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        pygame.image.load("assets/table.png")
        pygame.transform.scale(pygame.image.load("assets/table.png"), (800, 600))
        screen.blit(pygame.transform.scale(pygame.image.load("assets/table.png"), (800, 600)), (0, 0))

        draw_all__cards(screen)

        pygame.display.flip()

    pygame.quit()

main()