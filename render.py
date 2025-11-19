import os
from PIL import Image, ImageDraw, ImageFont

def generate_custom_card(health, damage, name, base):

    base_path = f"assets/cards/images/{base}.png"
        
    base_card = Image.open(base_path).convert("RGBA")
    draw = ImageDraw.Draw(base_card)
    card_width, card_height = base_card.size
    title_font = ImageFont.truetype("assets/font/Baskervville-Italic-VariableFont_wght.ttf", 40) 
    stat_font = ImageFont.truetype("assets/font/Baskervville-Italic-VariableFont_wght.ttf",45)    
    number_font = ImageFont.truetype("assets/font/Baskervville-Italic-VariableFont_wght.ttf", 100) 

    name_y = int(card_height * 0.08)

    stat_line_y = int(card_height * 0.78)
    health_x = int(card_width * 0.25)
    damage_x = int(card_width * 0.75)
    number_y = int(card_height * 0.88)

    draw.text((card_width/2, name_y), name.upper(), fill="#000000", font=title_font, anchor="mm", align="center")
    draw.text((health_x, stat_line_y), "HEALTH", fill="#000000", font=stat_font, anchor="ms", align="center")
    draw.text((damage_x, stat_line_y), "DAMAGE", fill="#000000", font=stat_font, anchor="ms", align="center")
    draw.text((health_x, number_y), health, fill="#000000", font=number_font, anchor="ms", align="center")
    draw.text((damage_x, number_y), damage, fill="#000000", font=number_font, anchor="ms", align="center")
    
    base_card.save(f'assets/cards/out/{base}')


if __name__ == '__main__':
    os.makedirs("assets/cards", exist_ok=True) 

    generate_custom_card(
        health="1500", 
        damage="8000", 
        name="The Mighty Python", 
        base=0,
    )