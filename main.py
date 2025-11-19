import pygame
import time
import random
from assets.data.stats import cards_id_reference
from render import generate_custom_card

# ------------------ Card Utilities ------------------
def get_card(id):
    return cards_id_reference[id]

def create_card_instance(id):
    base_card = get_card(id)
    return {
        "id": id,
        "name": base_card["name"],
        "hp": base_card["hp"]*2,
        "dmg": base_card["dmg"]//2,
        "stars": base_card.get("stars", 0),
        "artifacts": base_card.get("artifacts", [])
    }

player_cards = [create_card_instance(random.randint(1,9)) for i in range(3)]
enemy_cards = [create_card_instance(random.randint(1,9)) for i in range(3)]

# ------------------ Drawing ------------------
def draw_card(screen, position, card_instance, card_width=120):
    try:
        card_path = f"assets/cards/out/{card_instance['id']}.png"
        card_image = pygame.image.load(card_path)
    except:
        generate_custom_card(
            health=str(card_instance["hp"]),
            damage=str(card_instance["dmg"]//2),
            name=card_instance["name"],
            base=card_instance["id"],
        )
        card_path = f"assets/cards/out/{card_instance['id']}.png"
        card_image = pygame.image.load(card_path)

    orig_width, orig_height = card_image.get_size()
    scale_factor = card_width / orig_width
    card_height = int(orig_height * scale_factor)
    card_image = pygame.transform.scale(card_image, (card_width, card_height))

    screen.blit(card_image, position)

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(position[0], position[1], card_width, card_height), 2)

def draw_all_cards(screen):
    card_width = 240
    spacing = 20
    total_player_width = len(player_cards) * card_width + (len(player_cards) - 1) * spacing
    start_x_player = (screen.get_width() - total_player_width) // 2
    y_player = screen.get_height() - 370

    for idx, card in enumerate(player_cards):
        x = start_x_player + idx * (card_width + spacing)
        draw_card(screen, (x, y_player), card, card_width)

    total_enemy_width = len(enemy_cards) * card_width + (len(enemy_cards) - 1) * spacing
    start_x_enemy = (screen.get_width() - total_enemy_width) // 2
    y_enemy = 20

    for idx, card in enumerate(enemy_cards):
        x = start_x_enemy + idx * (card_width + spacing)
        draw_card(screen, (x, y_enemy), card, card_width)


# ------------------ Battle Logic ------------------
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

# ------------------ Main Loop ------------------
def main():
    pygame.init()
    screen_width, screen_height = 1200, 760
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cards of Cuthulhu")

    table_image = pygame.image.load("assets/table.png")
    table_image = pygame.transform.scale(table_image, (screen_width, screen_height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move()

        screen.blit(table_image, (0, 0))

        draw_all_cards(screen)

        

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
