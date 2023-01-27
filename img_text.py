import cv2
import pytesseract
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw() #hiding the tkinter window
img = filedialog.askopenfilename() #open the file dialog to select the image
img1 = cv2.imread(img) #read the selected image

if img1 is not None:
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #convert image to grayscale
    text = pytesseract.image_to_string(gray) #extract text from grayscale image
    print(text) #print the extracted text
else:
    print("Please select correct input") #if image is not selected
