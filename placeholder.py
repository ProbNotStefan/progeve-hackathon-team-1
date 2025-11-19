import os
from PIL import Image

def create_placeholder_image(width, height, filename="placeholder_art.jpg", color="white"):
    """
    Creates a solid color image (default white) of specified dimensions.

    This file can be used as the 'image_path' argument in the generate_custom_card script.

    Args:
        width (int): The width of the placeholder image in pixels.
        height (int): The height of the placeholder image in pixels.
        filename (str): The name of the file to save (e.g., 'placeholder.jpg').
        color (str): The color of the image (e.g., 'white', 'black', 'red', etc.).
    """
    try:
        # Create a new RGB image with the specified dimensions and color
        img = Image.new('RGB', (width, height), color=color)
        
        # Save the image
        img.save(filename)
        print(f"Successfully created placeholder image: {filename} ({width}x{height})")
        
    except Exception as e:
        print(f"Error creating placeholder image: {e}")

if __name__ == '__main__':
    # Define the dimensions for the placeholder art.
    # It's good practice to make this large enough to be scaled down gracefully.
    placeholder_width = 100
    placeholder_height = 50
            
    # Run the function to create 'character_art.jpg', matching the name used
    # in the example of your main card script.
    create_placeholder_image(
        width=placeholder_width, 
        height=placeholder_height, 
        filename="assets/cards/images/placeholder.jpg"
    )
    
    # You can also create a different sized one easily
    # create_placeholder_image(50, 50, "small_icon.png", "gray")