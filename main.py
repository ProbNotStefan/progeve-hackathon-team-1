import pygame
import assets.data.stats as stats
from assets.data.stats import cards_id_reference
from render import generate_custom_card

def get_card(id):
    return cards_id_reference[id]
    
def create_card_instance(id):
    base_card = get_card(id)
    return {
        "id": id,
        "name": base_card["name"],
        "hp": base_card["hp"],
        "dmg": base_card["dmg"],
        "stars": base_card.get("stars", 0),
        "artifacts": base_card.get("artifacts", [])
    }

player_cards = [create_card_instance(0), create_card_instance(1), create_card_instance(2)]
enemy_cards = [create_card_instance(3), create_card_instance(4), create_card_instance(5)]




def draw_card(screen, position, card_instance):
    card_color = (255, 255, 255)
    card_rect = pygame.Rect(position[0], position[1], 100, 150)

    card_path = f"assets/cards/live/{card_instance['id']}.png"
    try:
        card_image = pygame.image.load(card_path)
        card_image = pygame.transform.scale(card_image, (100, 150))
        screen.blit(card_image, position)
    except:
        generate_custom_card(
            health=str(card_instance["hp"]),
            damage=str(card_instance["dmg"]),
            name=card_instance["name"],
            image_path=f"assets/cards/{card_instance['id']}.png",
            output_filename=card_path
        )
        card_image = pygame.image.load(card_path)
        card_image = pygame.transform.scale(card_image, (100, 150))
        screen.blit(card_image, position)

    pygame.draw.rect(screen, card_color, card_rect)


    

def draw_all__cards(screen):
    for idx, id in enumerate(player_cards):
        draw_card(screen, (50 + idx * 110, 400), id)
    for idx, id in enumerate(enemy_cards):
        draw_card(screen, (50 + idx * 110, 50), id)


        

def move():
    for idx in range(len(player_cards)-1, -1, -1):
        card = player_cards[idx]
        if enemy_cards:
            enemy_card = enemy_cards[min(len(enemy_cards)-1, idx)]
            enemy_card["hp"] -= card["dmg"]
            if enemy_card["hp"] <= 0:
                enemy_cards.pop(0)
        if card["hp"] <= 0:
            player_cards.pop(idx)

    for idx in range(len(enemy_cards)-1, -1, -1):
        card = enemy_cards[idx]
        if player_cards:
            player_card = player_cards[min(len(player_cards)-1, idx)]
            player_card["hp"] -= card["dmg"]
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