from PIL import Image, ImageFont, ImageDraw
from string import *


def main():
    file = open('trainingLists.txt', 'w')
    fontList = [ImageFont.truetype("C:\Windows\Fonts\OCRAEXT.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AGENCYR.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\ARIALUNI.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\Hack-Regular.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\FTLTLT.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\GARA.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\REFSAN.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\VINERITC.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\times.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\timesi.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\trebuc.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\Tiger.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\Tiger Expert.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\TEMPSITC.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\tahoma.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\\TektonPro-BoldCond.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AdobeHebrew-Regular.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AdobeArabic-Regular.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AdobeArabic-Bold.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\SourceSansPro-Regular.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\Sitka.ttc", 18),
                ImageFont.truetype("C:\Windows\Fonts\MOD20.ttf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AdobeMingStd-Light.otf", 18),
                ImageFont.truetype("C:\Windows\Fonts\AdobeSongStd-Light.otf", 18),
                ]

    for font in fontList:
        for character in ascii_letters:
            im = Image.open("empty.png")
            draw = ImageDraw.Draw(im)
            draw.text((4, 0), character, (0, 0, 0), font=font)
            saveName = "training letters/" + font.getname()[0] + character + str(ord(character)) + ".png"
            im.save(saveName)
            im = im.convert('1')
            pixelList = list(im.getdata())
            for x in range(len(pixelList)):
                pixelList[x] = int(not(pixelList[x] // 255))
            print(character, pixelList, file=file)

if __name__ == "__main__":
    main()