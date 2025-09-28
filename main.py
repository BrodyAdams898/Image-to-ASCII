from PIL import Image
from pathlib import Path

#* Display available images to convert
images_folder = Path("images")
image_files = [f for f in images_folder.iterdir() if f.suffix.lower() in [".png", ".jpg", ".jpeg"]]
for file in image_files:
    print(file.name)

#* Open and set image scale
im_path = "images/" + str(input("Enter the full name of your image form the 'images/' directory: "))
im = Image.open(im_path).convert("RGB") # Drop alpha channel if it exist
print(im.format, im.size, im.mode)

im_scale = float(input("Enter the images scale (Recommended 0.1 - 0.3): "))

im_width = int(im.width * im_scale)
im_height = int(im.height * im_scale)
im_size = (im_width, im_height)

im = im.resize(im_size)

input(f"New Size is: {im_size}, Press ENTER to print")


ascii_chars = "─=#▒██"
num_of_chars = len(ascii_chars)

# # y = row, x = Element in row
# # Easier to visualize initialization of matrixes as a for-loop
# rgb_matrix = []
# for y in range(im_height):
#     row = []
#     for x in range(im_width):
#         row.append(im.getpixel)
#     rgb_matrix.append(row)

def getPixelBrightness(x, y):
    rgb_value = im.getpixel((x, y))
    return int(sum(rgb_value) / 3)

def convertToAscii(ascii_chars, num_of_chars, brightness):
    index = int((brightness / 255) * (num_of_chars - 1))
    return ascii_chars[index]

rgb_matrix = [[im.getpixel((x, y)) for x in range(im_width)] for y in range(im_height)]

brightness_matrix = [[getPixelBrightness(x, y) for x in range(im_width)] for y in range(im_height)]

ascii_matrix = [[convertToAscii(ascii_chars, num_of_chars, brightness_matrix[y][x]) for x in range(im_width)] for y in range(im_height)]

# Print ASCII image
for y in range(im_height):
    for x in range(im_width):
        print(ascii_matrix[y][x] * 2, end='')
    print()