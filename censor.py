import random as rd


def censor_subtitles(file_name, percentage):
    """
    This function censors a specified percentage of subtitles in a given .srt file.
    It writes the censored subtitles to a new file while retaining some original subtitles to aid language learning by providing context.
    """
    # Attempt to open the original subtitle file
    try:
        with open(f"{file_name}.srt", "r", encoding="utf-8") as file:
            # Create a new file for the censored subtitles
            with open(f"[censored] {file_name}.srt", "w", encoding="utf-8") as new_file:
                censor = False  # Indicates when we are in a subtitle segment, changes to True when detecting '-->' in a line (it means the next lines are subtitles)
                print("\nThe file was found. The file is now being edited...")

                for line in file:
                    if not censor:
                        new_file.write(line)  # Write the current line to the new file
                        # Check if the line indicates the start of a new subtitle segment
                        if len(line) > 16 and line[13:16] == "-->":
                            censor = True

                    else:
                        if line == "\n":  # End of a subtitle segment
                            censor = False
                            new_file.write(line)
                            continue

                        # Censor words in the current subtitle line based on the given percentage
                        censored_line = censor_line(line, percentage)
                        new_file.write(censored_line)

        print("Censorship complete! New file created: [censored] {}.srt".format(file_name))
    
    except FileNotFoundError:
        print("Error: The specified file was not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def censor_line(line, percentage):
    """This function censors individual words in a line based on the specified percentage."""
    line_list = line.split()
    censored_words = [
        "*" if rd.random() < percentage / 100 else word for word in line_list
    ]
    return " ".join(censored_words) + "\n"


if __name__ == "__main__":
    # Get user input for the file name and censoring percentage
    file_name = input("Name of the .srt file with the subtitles: ")
    percentage = float(input("Percentage of subtitles to censor (0-100): "))

    censor_subtitles(file_name, percentage)

    input("Process ended! Press ENTER to close.")
