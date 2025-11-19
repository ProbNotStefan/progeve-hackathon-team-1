import os
from PIL import Image, ImageDraw, ImageFont

def generate_custom_card(health, damage, name, image_path, output_filename="custom_card.png"):
    
    base_path = "assets/cards/base.png"
    image_path = "assets/cards/images/" + image_path
        
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

    image_area_box = (
        int(card_width * 0.01),   # Left X
        int(card_height * 0.12),  # Top Y
        int(card_width * 0.95),   # Right X
        int(card_height * 0.65)   # Bottom Y
    )
    
    custom_img = Image.open(image_path).convert("RGBA")
    
    box_width = image_area_box[2] - image_area_box[0]
    box_height = image_area_box[3] - image_area_box[1]

    custom_img = custom_img.resize((box_width, box_height), Image.Resampling.LANCZOS)

    base_card.paste(custom_img, (image_area_box[0], image_area_box[1]), custom_img)

    draw.text((card_width/2, name_y), name.upper(), fill="#000000", font=title_font, anchor="mm", align="center")
    draw.text((health_x, stat_line_y), "HEALTH", fill="#000000", font=stat_font, anchor="ms", align="center")
    draw.text((damage_x, stat_line_y), "DAMAGE", fill="#000000", font=stat_font, anchor="ms", align="center")
    draw.text((health_x, number_y), health, fill="#000000", font=number_font, anchor="ms", align="center")
    draw.text((damage_x, number_y), damage, fill="#000000", font=number_font, anchor="ms", align="center")
    
    base_card.save(f"assets/cards/out/{output_filename}")


if __name__ == '__main__':
    os.makedirs("assets/cards", exist_ok=True) 

    generate_custom_card(
        health="15", 
        damage="8", 
        name="The Mighty Python", 
        image_path="placeholder.jpg", 
        output_filename="python_hero_card_large_font.png"
    )