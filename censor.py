import random as rd

"""
When we give the script a .srt subtitle file, this will create a new file, with some of the subtitles being censored.
This will help the language learner, by slowly acquiring the language (like a child learns).
It also gives them some help (since some subtitles will not be censored), but forces them to understand the context of the scene to understand the censored words.
"""

file_name = input("Name of the .srt file with the subtitles: ")
percentage = float(input("Percentage of subtitles to censor: "))

file = open("{}.srt".format(file_name), "r")  # open subtitle file in reading mode
new_file = open("[censored] {}.srt".format(file_name), "w")  # create new file to write new subtitles
censor = False  # changes to True when detecting '-->' in a line and returns to False when a linew only has '\n'
print("\nThe file was found. The file is now being edited...")

while True:
    line = file.readline()  # readds the next line
    if line == "":
        break  # if the file ends, break the while cycle

    if not censor:
        new_file.write(line)  # add line to the new file
        if len(line) > 16:
            if line[13:16] == "-->":
                censor = True

    elif censor:
        if line == "\n":
            censor = False
            new_file.write(line)
            continue  # continues to next iteration, skipping the steps below (this line is not edited)
        line_list = line.split()
        new_line = ""
        for j in range(len(line_list)):
            if rd.random() < percentage / 100:
                line_list[j] = "*"  # replaces word by '*'
            new_line += (line_list[j] + " ")  # add word (edited or not) to new line
        new_line += "\n"
        new_file.write(new_line)

# close used files - always needed when editing
file.close()
new_file.close()
x = input("Process ended! Press ENTER to close.")