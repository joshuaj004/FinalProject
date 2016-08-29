from PIL import Image, ImageFont, ImageDraw
from string import *

file = open("trainingLists.txt", 'r')
wordDict = {}
for line in file:
    letter, matrix = line.split(" [")
    matrix = '['  + matrix.strip()
    wordDict[matrix] = letter

fileName = input("Please enter the file name to analyze: ")
while fileName != '':
    im = Image.open(fileName)
    im = im.convert('1')
    pixelList = list(im.getdata())
    for x in range(len(pixelList)):
        pixelList[x] = int(not(pixelList[x] // 255))
    print("Is your letter " + wordDict[str(pixelList)] + "?")
    fileName = input("Please enter the file name to analyze: ")