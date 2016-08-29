import pprint
import classifiers
from PIL import Image, ImageFont, ImageDraw
import ast
import copy

DEBUG = True

def main():
    global recog_dict
    print("Preparing...")
    classifierFile = open("classifiers.txt", 'r')
    recog_dict = {}
    while True:
        matrix = classifierFile.readline().strip()
        characteristics = classifierFile.readline().strip()
        if matrix != '':
            recog_dict[matrix] = characteristics
        if not characteristics: break
    classifierFile.close()
    print("Ready for input.")
    fileName = input("Please enter file to analyze name or (q) to quit: ")
    while fileName != 'q':
        im = Image.open(fileName)
        im = im.convert('1')
        width, height = im.size
        if width > 21:
            multi_image(im)
        else:
            pixelList = list(im.getdata())
            for x in range(len(pixelList)):
                pixelList[x] = int(not(pixelList[x] // 255))
            closestMatch, exact = get_closest(str(pixelList))
            if DEBUG:
                newIm = Image.new('1', (40, 20))
                newIm.paste(im, (0, 0))
                tempDraw = ImageDraw.Draw(newIm)
                tempDraw.text((20, 0), closestMatch, 1, font=ImageFont.truetype("C:\Windows\Fonts\OCRAEXT.ttf", 20))
                newIm.show()
            correct = input("Is this your letter: " + closestMatch + " (Y/N)? ")
            if correct.lower() == 'y':
                learner(str(pixelList), closestMatch)
            else:
                actualLetter = input("What is the actual letter, in the correct case: ")
                learner(str(pixelList), actualLetter)
        fileName = input("Please enter file to analyze name or (q) to quit: ")


def learner(matrix, actualLetter):
    classifierFile = open("classifiers.txt", 'a')
    classifiersList = []
    matrix = ast.literal_eval(matrix)
    classifiersList.append(classifiers.horizontal_position(matrix))
    classifiersList.append(classifiers.vertical_position(matrix))
    classifiersList.append(classifiers.on_pixels(matrix))
    classifiersList.append(classifiers.mean_horizontal_position(matrix))
    classifiersList.append(classifiers.mean_vertical_position(matrix))
    classifiersList.append(classifiers.mean_squared_horizontal_position(matrix))
    classifiersList.append(classifiers.mean_squared_vertical_position(matrix))
    classifiersList.append(actualLetter)
    print(matrix, file=classifierFile)
    print(classifiersList, file=classifierFile)
    classifierFile.close()


def multi_image(image):
    newImg = Image.new("1", (200, 200), "black")
    draw = ImageDraw.Draw(newImg)
    font = ImageFont.truetype("C:\Windows\Fonts\OCRAEXT.ttf", 18)
    characterList = []
    for y in range(10):
        for x in range(10):
            crop_rectangle = (x * 20, y * 20, 20 + 20 * x, 20 + 20 * y)
            cropped_im = image.crop(crop_rectangle)
            pixelList = list(cropped_im.getdata())
            for x in range(len(pixelList)):
                pixelList[x] = int(not(pixelList[x] // 255))
            closestMatch, exact = get_closest(str(pixelList))
            characterList.append(closestMatch)
        print((1+y) * 10, "% complete")
    counter = 0
    for y in range(10):
        for x in range(10):
            character = characterList[counter]
            counter += 1
            draw.text((4 + 20 * x, 0 + 20 * y), character, 1, font=font)
    newImg.show()


def get_closest(matrix):
    if matrix in recog_dict:
        answerMatrix = ast.literal_eval(recog_dict[matrix])
        return answerMatrix[-1], True
    classifiersList = []
    matrix = ast.literal_eval(matrix)
    classifiersList.append(classifiers.horizontal_position(matrix))
    classifiersList.append(classifiers.vertical_position(matrix))
    classifiersList.append(classifiers.on_pixels(matrix))
    classifiersList.append(classifiers.mean_horizontal_position(matrix))
    classifiersList.append(classifiers.mean_vertical_position(matrix))
    classifiersList.append(classifiers.mean_squared_horizontal_position(matrix))
    classifiersList.append(classifiers.mean_squared_vertical_position(matrix))
    # Go through each classifier and eliminate those that are out of range of the test element
    tempDict = dict.fromkeys(recog_dict, 0)
    for x in range(7):
        first, second, third = get_ranges(classifiersList[x])
        for tempMatrix in tempDict:
            answerMatrix = ast.literal_eval(recog_dict[tempMatrix])
            checkValue = answerMatrix[x]
            if first[0] <= checkValue <= first[1]:
                tempDict[tempMatrix] += 3
            elif second[0] <= checkValue <= second[1]:
                tempDict[tempMatrix] += 2
            elif third[0] <= checkValue <= third[1]:
                tempDict[tempMatrix] += 1
            else:
                tempDict[tempMatrix] -= 1
    largest = max(tempDict, key=tempDict.get)
    tempDict1 = dict.fromkeys(recog_dict, 0)
    for tempMatrix in tempDict1:
        answerMatrix = ast.literal_eval(tempMatrix)
        closeness = classifiers.cosine_similarity(answerMatrix, matrix)
        tempDict[tempMatrix] += int(15 * closeness)
        tempDict1[tempMatrix] = closeness
    newLargest = max(tempDict, key=tempDict.get)
    tempLargest = max(tempDict1, key=tempDict1.get)
    return ast.literal_eval(recog_dict[newLargest])[-1], False


def get_ranges(value):
    first = (int(value - 0.1 * value), int(value + 0.1 * value))
    second = (int(value - 0.2 * value), int(value + 0.2 * value))
    third = (int(value - 0.3 * value), int(value + 0.3 * value))
    return first, second, third


main()