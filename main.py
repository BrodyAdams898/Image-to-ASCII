from PIL import Image
im = Image.open("images/ascii-pineapple.jpg")
print(im.format, im.size, im.mode)

scale = 0.2

im_width = int(im.width * scale)
im_height = int(im.height * scale)
im_size = (im_width, im_height)

im = im.resize(im_size)
print(f"New Size is: {im_size}")

# y = row, x = column(Element in row)

def getPixelBrightness(x, y):
    rgb_value = im.getpixel((x, y)) #rgb_value now equals a tuple like (255, 39, 0)    
    return int(sum(rgb_value) / 3)

brightness_matrix = [[getPixelBrightness(x, y) for x in range(im_width)] for y in range(im_height)]

# # Alternative readable version of code above using nested loops:
#
# pixel_matrix = []
# for y in range(im_height):
#     row = []
#     for x in range(im_width):
#         row.append(im.getpixel((x, y)))
#     pixel_matrix.append(row)
#
# brightness_matrix = []
# for y in range(im_height):
#     row = []
#     for x in range(im_width):
#         row.append(sum(pixel_matrix[y][x]) / 3)
#     brightness_matrix.append(row)

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
num_of_chars = len(ascii_chars)

def convertToAscii(ascii_chars, num_of_chars, brightness):
    index = int((brightness / 255) * (num_of_chars - 1))
    return ascii_chars[index]

ascii_matrix = []
for y in range(im_height):
    row = []
    for x in range(im_width):
        row.append(convertToAscii(ascii_chars, num_of_chars, brightness_matrix[y][x]))
    ascii_matrix.append(row)

for y in range(im_height):
    for x in range(im_width):
        print(ascii_matrix[y][x] * 2, end='')
    print()



