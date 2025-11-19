import pygame
import assets.data.stats as stats
from stats import cards_id_reference
from render import generate_custom_card

def get_card(id):
    return cards_id_reference[id]
    

player_cards = [get_card(0), get_card(1), get_card(2)]
enemy_cards = [get_card(3), get_card(4), get_card(5)]

def draw_card(screen, position, id):
    card_color = (255, 255, 255)
    card_rect = pygame.Rect(position[0], position[1], 100, 150)

    card = f"assets/cards/live/{id}.png"
    try:
        card_image = pygame.image.load(card)
        card_image = pygame.transform.scale(card_image, (100, 150))
        screen.blit(card_image, position)
    except:
        generate_custom_card(
            health=str(cards_id_reference[id]["hp"]),
            damage=str(cards_id_reference[id]["dmg"]),
            name=cards_id_reference[id]["name"],
            image_path="assets/cards/default_art.png",
            output_filename=card
        )
        card_image = pygame.image.load(card)
        card_image = pygame.transform.scale(card_image, (100, 150))
        screen.blit(card_image, position)

    pygame.draw.rect(screen, card_color, card_rect)
    

def draw_all__cards(screen):
    for idx, id in enumerate(player_cards):
        draw_card(screen, (50 + idx * 110, 400), id)
    for idx, id in enumerate(enemy_cards):
        draw_card(screen, (50 + idx * 110, 50), id)


        

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