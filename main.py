from PIL import Image

# Open and set image scale
im = Image.open("images/ascii-pineapple.jpg")
print(im.format, im.size, im.mode)

scale = 0.1

im_width = int(im.width * scale)
im_height = int(im.height * scale)
im_size = (im_width, im_height)

im = im.resize(im_size)
print(f"New Size is: {im_size}")


ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
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