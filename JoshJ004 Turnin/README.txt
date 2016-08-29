README.TXT for OCRMain.py
This is a simple OCR (Optical Character Recognition) program made in Python.
It depends on the following .py files:
    1. training_creator.py
    2. classifiers.py
    3. classifier_handler.py
    
It depends on the existence of the following .txt files:
    1. classifiers.txt
    2. trainingLists.txt

It depends on the following libraries:
    1. pprint
    2. PIL: Image, ImageFont, ImageDraw
    3. ast
    4. copy
    5. string
    6. math
    7. scipy
    8. numpy
    9. unittest
    
training_creator.py requires a multitude of fonts, however the fonts can be 
replaced with what the user has installed on their computer, downloaded, or 
the user can omit those fonts. Alternatively, if the classifiers.txt file is 
present, one can ignore the use of training_creator.py

Currently OCRMain.py can take two types of files as input. The first is a 20x20
png file and the second is a collection of 20x20 characters (font size 18) in
a 200x200 png file. If it is the first, the user will be shown the closest 
match and asked if this is the correct character. If it is, the letter is now
incorporated in the classifiers.txt. If it isn't, the user is asked to input
the correct character in the correct case, which is then saved in 
classifiers.txt. If the user inputs a 200x200 image, then the program 
iterates through and finds the closest match for each character found
and stitches this together in a new image which is then showed to the user.
