import pygame
import assets.data.stats as stats

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
    return stats.cards_id_reference[id]

def move():
    for idx, card in enumerate(player_cards):
        damage = card["dmg"]
        if enemy_cards:
            enemy_card = get_card(enemy_cards[idx])
            enemy_card["hp"] -= damage
            if enemy_card["hp"] <= 0:
                enemy_cards.pop(0)
        if card["hp"] <= 0:
            player_cards.pop(idx)
    
    for idx, card in enumerate(enemy_cards):
        damage = card["dmg"]
        if player_cards:
            player_card = get_card(player_cards[idx])
            player_card["hp"] -= damage
            if player_card["hp"] <= 0:
                player_cards.pop(0)
        if card["hp"] <= 0:
            enemy_cards.pop(idx)




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