# Beginner Text Cataract Visualizer
# This is a text only version. It is not realistic for actual vision
# Designed as a learning project to understand image/text processing in Python
# Author: Jaedyn Carbonell

def blur_text(text, severity=1):
    """
    Add spaces after letters to simulate blur
    :param text: The input text to blur
    :param severity: How strong the "blur" is/number of spaces after each letter
    :return: The blurred text
    """
    newText = ""
    for char in text:
        newText += char
        if char.isalpha():
            newText += " " * severity
    return newText

def haze_text(text, severity=1):
    """
    Replace some letters with dots to simulate haze/faded vision
    :param text: The input text to haze
    :param severity: How many letters to replace with dots
    :return: The hazy text
    """
    newText = ""
    for char in text:
        if char.isalpha() and severity > 0:
            newText += "."
            severity -= 1
        else:
            newText += char
    return newText

def simulate_cataract(text, severity=1):
    """
    Combine blur and haze for a simple cataract effect
    :param text: The input text
    :param severity: Severity of the cataract effect from 1 to 5
    :return: Text with simulated cataract
    """
    blurred = blur_text(text, severity)
    hazy = haze_text(blurred, severity * 2)  # more haze if severity is larger
    return hazy

if __name__ == "__main__":
    print("Text Cataract Simulator")
    userText = input("Enter the text you want to simulate: ")
    while True:
        try:
            severity = int(input("Enter severity (1-5, 1 = mild, 5 = strong): "))
            if 1 <= severity <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

    simulated = simulate_cataract(userText, severity)
    print("\nNormal Vision:    ", userText)
    print("Simulated Cataract:", simulated)
