from PIL import Image, ImageFont, ImageFilter, ImageDraw
from matplotlib.pyplot import draw
import numpy as np
import os
from fontTools.ttLib import TTFont

digits = ['1','2','3','4','5','6','7','8','9']
WIDTH = 100
HEIGHT = 100
count = 0

def generateCharacter(path, digit, fontPath):
    background_color = min(int((200 + np.random.normal() * 20)), 255)
    digit_color = int(15 + np.random.normal() * 20)
    image = Image.new("L", (WIDTH, HEIGHT), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontPath, 50)

    w, h = draw.textsize(digit, font)
    draw.text(((WIDTH-w) / 2, (HEIGHT-h) / 2), digit, (digit_color,), font)
    
    digitLeft = WIDTH
    digitTop = HEIGHT
    digitRight = 0
    digitBottom = 0

    pixels = image.load()
    for col in range(image.size[0]):
        for row in range(image.size[1]):
            if(pixels[col, row] != background_color):
                digitLeft = min(col, digitLeft)
                digitTop = min(row, digitTop)
                digitRight = max(col, digitRight)
                digitBottom = max(row, digitBottom)

    image = image.filter(ImageFilter.GaussianBlur(1.2))
    image = image.crop((digitLeft - 3, digitTop - 2, digitRight + 3, digitBottom + 2))
    
    cropped_pixels = image.load()
    for col in range(image.size[0]):
        for row in range(image.size[1]):
            val = cropped_pixels[col, row] + (np.random.normal() * 5)
            cropped_pixels[col, row] = (int(val),)

    image.save(f"{path}/{count}.png")


blacklist = [
    "rubik", 
    "librebarcode", 
    "blakahollow", 
    "bungeeshade",
    "rougescript",
    "codystar",
    "montserrat",
    "fasterone",
    "redacted",
    "londrina",
    "slab",
    "flowcircular",
    "rampartone",
    "monofett",
    "jacquesfrancois",
    "tourney",
    "nosifer",
    "plaster",
    "love",
    "moolahlah",
    "bungee",
    "neonderthaw",
    "flow",
    "hanalei",
    "zentokyo",
    "ballet",
    "kenia",
    "geostar",
    "noto",
    "d0500",
    "karumbi",
    "italic",
    "sevillana",
    "waterbrush-regular",
    "sixcaps",
    "jsmath",
    "ewert",
    "sniglet-extrabold",
    "rock3d-regular",
    "qwitchergrypen",
    "silkscreen-bold",
    "akronim",
    "smokum",
    "wireone",
    "/oi-regular.ttf",
    "fenix",
    "butterflykids",
    "anybody[wdth,wght]",
    "stalinistone",
    "bigshouldersinline",
    "sunshiney",
    "portersansblock",
    "miltonian",
    "chokokutai"
]

digitOrdinals = [ord(digit) for digit in digits]
def fontSupportsDigits(fontPath) -> bool:
    font = TTFont(fontPath)
    for table in font["cmap"].tables:
        for o in digitOrdinals:
            if o not in table.cmap.keys():
                return False
            return True

def blacklisted(fontPath) -> bool:
    for keyword in blacklist:
        if keyword in fontPath.lower():
            return True
    return False

imageFontMap = []

with open("fonts/font_list.txt", "r") as fontPaths:
    for fontPath in fontPaths:
        fontPath = fontPath.strip()
        if(fontSupportsDigits(fontPath) and not blacklisted(fontPath)):
            for digit in digits:
                path = f"testing_data/{digit}" if count%10==0 else f"training_data/{digit}"
                imageFontMap.append(f"{path}/{count}.png : {fontPath}")
                os.makedirs(path, exist_ok=True)
                generateCharacter(path, digit, fontPath)
                count = count + 1

with open("image_to_font_map.txt", "w") as map_file:
    map_file.write("\n".join(imageFontMap))