from PIL import Image
from pathlib import Path
from prompt_toolkit.shortcuts import radiolist_dialog


#* Display available images to convert
images_folder = Path("images")
image_files = [file for file in images_folder.iterdir() if file.suffix.lower() in [".png", ".jpg", ".jpeg"]]

option_list = []
for file in image_files:
    option = (file, str(file).replace("images\\", "").replace("images/", ""))
    print(option[1])
    option_list.append(option)


# im = Image.open(file_path).convert("RGB")
# print(im.format, im.size, im.mode)
#* Set  scale
im_scale = float(input("Enter the images scale (Recommended 0.1 - 0.3): "))

im_width = int(im.width * im_scale)
im_height = int(im.height * im_scale)
im_size = (im_width, im_height)

im = im.resize(im_size)

input(f"New Size is: {im_size}, Press ENTER to print")



#* Set ASCII characters
ascii_chars = "─=#▒██"
num_of_chars = len(ascii_chars)

def getPixelBrightness(x, y):
    rgb_value = im.getpixel((x, y))
    return int(sum(rgb_value) / 3)

def convertToAscii(ascii_chars, num_of_chars, brightness):
    index = int((brightness / 255) * (num_of_chars - 1))
    return ascii_chars[index]

rgb_matrix = [[im.getpixel((x, y)) for x in range(im_width)] for y in range(im_height)]

brightness_matrix = [[getPixelBrightness(x, y) for x in range(im_width)] for y in range(im_height)]

ascii_matrix = [[convertToAscii(ascii_chars, num_of_chars, brightness_matrix[y][x]) for x in range(im_width)] for y in range(im_height)]

# # y = row, x = Element in row
# # Easier to visualize initialization of matrixes as a for-loop
# rgb_matrix = []
# for y in range(im_height):
#     row = []
#     for x in range(im_width):
#         row.append(im.getpixel)
#     rgb_matrix.append(row)

# Print ASCII image
for y in range(im_height):
    for x in range(im_width):
        print(ascii_matrix[y][x] * 2, end='')
    print()