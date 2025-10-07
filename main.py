"""
ASCII Art Converter

This script converts images to ASCII art by:
1. Loading images from the 'images' folder
2. Allowing user to select an image via an interactive menu
3. Resizing the image based on user input
4. Converting pixel brightness to ASCII characters
5. Displaying the resulting ASCII art in the terminal
"""

from PIL import Image
from pathlib import Path
from menu import TerminalMenu

# Set up the images folder path
images_folder = Path("images")

# Find all image files in the images folder (PNG, JPG, JPEG)
image_files = [
    file for file in images_folder.iterdir()
    if file.suffix.lower() in [".png", ".jpg", ".jpeg"]
]

# Create a list of image filenames for the menu
option_list = []
for file in image_files:
    # Remove the folder path to display only the filename
    option = str(file).replace("images\\", "").replace("images/", "")
    option_list.append(option)

# Exit if no images are found
if not option_list:
    print("No images found in the images folder!")
    exit()

# Display menu and get user's image selection
menu = TerminalMenu(option_list, title="=== Select an Image to Convert ===")
selected_image = menu.run()

# Exit if user didn't select anything
if selected_image is None:
    print("No selection made.")
    exit()

# Construct the full file path
file_path = images_folder / selected_image

# Open the image and convert to RGB mode
im = Image.open(file_path).convert("RGB")
print(im.format, im.size, im.mode)

# Get the scale factor from the user
im_scale = float(input("Enter the images scale (Recommended 0.1 - 0.3): "))

# Calculate new dimensions based on the scale
im_width = int(im.width * im_scale)
im_height = int(im.height * im_scale)
im_size = (im_width, im_height)

# Resize the image
im = im.resize(im_size)

# Wait for user confirmation before printing
input(f"New Size is: {im_size}, Press ENTER to print")

# ASCII characters to use for conversion (from light to dark)
ascii_chars = "─=#▒██"
num_of_chars = len(ascii_chars)


def getPixelBrightness(x, y):
    """
    Calculate the brightness of a pixel at given coordinates.
    
    Args:
        x (int): X coordinate of the pixel
        y (int): Y coordinate of the pixel
    
    Returns:
        int: Average brightness value (0-255)
    """
    rgb_value = im.getpixel((x, y))
    # Average the R, G, B values to get brightness
    return int(sum(rgb_value) / 3)


def convertToAscii(ascii_chars, num_of_chars, brightness):
    """
    Convert a brightness value to an ASCII character.
    
    Args:
        ascii_chars (str): String of ASCII characters (light to dark)
        num_of_chars (int): Number of characters in ascii_chars
        brightness (int): Brightness value (0-255)
    
    Returns:
        str: ASCII character representing the brightness
    """
    # Map brightness (0-255) to character index
    index = int((brightness / 255) * (num_of_chars - 1))
    return ascii_chars[index]


# Create a matrix of RGB values for each pixel
rgb_matrix = [[im.getpixel((x, y)) for x in range(im_width)] for y in range(im_height)]

# Create a matrix of brightness values for each pixel
brightness_matrix = [[getPixelBrightness(x, y) for x in range(im_width)] for y in range(im_height)]

# Convert brightness values to ASCII characters
ascii_matrix = [[
    convertToAscii(ascii_chars, num_of_chars, brightness_matrix[y][x])
    for x in range(im_width)
] for y in range(im_height)]

# Print the ASCII art to the terminal
for y in range(im_height):
    for x in range(im_width):
        # Print each character twice to compensate for character width
        print(ascii_matrix[y][x] * 2, end='')
    print()  # New line after each row
