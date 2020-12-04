import re

import cv2
import pytesseract

# refer to executable file ptesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\pwalavalkar\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('sample-pan-card-front.jpg')

# opencv is in BGR and pytesseract only accepts RGB value
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(img)

print(text)

text1 = []

# Treat every line obtained in text as a single string and create list from it
lines = text.split('\n')
print(lines)
for lin in lines:
    s = lin.strip()
    s = s.rstrip()
    s = s.lstrip()
    text1.append(s)
print(text1)

# Remove blank items from the list
text1 = list(filter(None, text1))
print("text1", text1)

data = {}
data["Name"] = text1[1]
data["Father Name"] = text1[2]
data['DOB'] = text1[3]
data['PAN'] = text1[5]

print('\t', "|+++++++++++++++++++++++++++++++|")
print('\t', '|', '\t', data['Name'])
print('\t', "|-------------------------------|")
print('\t', '|', '\t', data['Father Name'])
print('\t', "|-------------------------------|")
print('\t', '|', '\t', data['DOB'])
print('\t', "|-------------------------------|")
print('\t', '|', '\t', data['PAN'])
print('\t', "|+++++++++++++++++++++++++++++++|")
