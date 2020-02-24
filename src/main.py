import cv2

def main():
    detectShapesFromFrame("")
if __name__ == '__main__':
    main()


# Given a single frame of video recording, video stream, or single image file, detect the shapes inside of it.
def detectShapesFromFrame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)