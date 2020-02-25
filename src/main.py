import imghdr
import cv2
import os.path
from os import path
import tkinter as tk
import tkinter.filedialog


# Select mode
def selectMode():
    mode = input("Select Mode:\n"
                 "1 for Detecting Shapes from an image.\n"
                 "2 for Detecting Shapes inside all images in a directory\n"
                 "3 for Detecting Shapes from a Video Feed (i.e. webcam)\n"
                 "4 for Detecting Shapes from the shapes folder in this program's directory (default option)\n")
    if mode == 1:
        askforimage()


# Asks the user for an image file and validates that it is an image, then
# returns the path to the filename
def askforimage():
    # Ask for Image by opening a directory window
    filename = tk.filedialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    # print(root.filename)
    # Validation
    if validateimage(filename) == False:
        print("Unsupported image file type for image " + filename + ". Please try again.")
        askforimage()
    else: return filename

# Accepts an object with a filename.
# Returns True if file is a selected image type
# Returns False if the file is an invalid type
def validateimage(filename):
    imagetype = imghdr.what(filename).lower()
    supportedtypes = ["png", "jpeg", "jpg"]
    for type in supportedtypes:
        if imagetype == type:
            return True
    return False

# Given a single frame of video recording, video stream, or single image file, detect the shapes inside of it and return
# a frame with the shapes outlined and named.
def detectshapesfromframe(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    font = cv2.FONT_HERSHEY_COMPLEX

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(gray, [approx], 0, 0, 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        print(len(approx))  # prints the contour line amounts

        if len(approx) == 3:
            cv2.putText(gray, "Triangle", (x, y), font, 1, (0))

        elif len(approx) == 4:
            cv2.putText(gray, "Rectangle", (x, y), font, 1, (0))

        elif len(approx) == 5:
            cv2.putText(gray, "Pentagon", (x, y), font, 1, (0))

        elif len(approx) == 6:
            cv2.putText(gray, "Hexagon", (x, y), font, 1, (0))

        elif len(approx) == 10:
            cv2.putText(gray, "Star", (x, y), font, 1, (0))

        elif 6 < len(approx) <= 15:
            cv2.putText(gray, "Oval", (x, y), font, 1, (0))
        else:
            cv2.putText(gray, "Circle", (x, y), font, 1, (0))
    return gray

def main():
    selectMode()
if __name__ == '__main__':
    main()