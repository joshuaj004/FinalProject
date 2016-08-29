from classifiers import *
import ast


def main():
    inFile = open("trainingLists.txt", 'r')
    outFile = open("classifiers.txt", 'w')
    for line in inFile:
        letter, matrix = line.split(" [")
        matrix = '['  + matrix.strip()
        classifiersList = []
        # classified with horizontal_position, vertical_position, on_pixels, mean_horizontal_position,
        # mean_vertical_position
        # mean_squared_horizontal_position, mean_squared_vertical_position, cosine_similarity
        matrix = ast.literal_eval(matrix)
        classifiersList.append(horizontal_position(matrix))
        classifiersList.append(vertical_position(matrix))
        classifiersList.append(on_pixels(matrix))
        classifiersList.append(mean_horizontal_position(matrix))
        classifiersList.append(mean_vertical_position(matrix))
        classifiersList.append(mean_squared_horizontal_position(matrix))
        classifiersList.append(mean_squared_vertical_position(matrix))
        classifiersList.append(letter)
        print(matrix, file=outFile)
        print(classifiersList, file=outFile)


if __name__ == "__main__":
    main()