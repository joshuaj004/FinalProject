from PIL import Image, ImageFont, ImageDraw
from string import *
import random

im = Image.open("200x200.png")
draw = ImageDraw.Draw(im)
fontList = [#ImageFont.truetype("C:\Windows\Fonts\OCRAEXT.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\AGENCYR.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\ARIALUNI.ttf", 18),
#             #ImageFont.truetype("C:\Windows\Fonts\AHack-Italic.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\Hack-Regular.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\FTLTLT.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\GARA.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\REFSAN.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\\trebuc.ttf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\AdobeHebrew-Regular.otf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\AdobeArabic-Regular.otf", 18),
#             ImageFont.truetype("C:\Windows\Fonts\AdobeArabic-Bold.otf", 18),
             ImageFont.truetype("C:\Windows\Fonts\AdobeMyungjoStd-Medium.otf", 18),
             ImageFont.truetype("C:\Windows\Fonts\AdobeMingStd-Light.otf", 18),
             ImageFont.truetype("C:\Windows\Fonts\AdobeSongStd-Light.otf", 18),
             ImageFont.truetype("C:\Windows\Fonts\cour.ttf", 18),
             ImageFont.truetype("C:\Windows\Fonts\ChaparralPro-Regular.otf", 18),
            ]

for y in range(12):
    for x in range(12):
        character = random.choice(ascii_letters)
        font = random.choice(fontList)
        #draw.text((4 + 18 * x, 0 + 18 * y), character, (0, 0, 0), font=font)
        draw.text((4 + 20 * x, 0 + 20 * y), character, (0, 0, 0), font=font)

im.save("200testerpic3.png")