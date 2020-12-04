import cv2
import pytesseract

# refer to executable file ptesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\pwalavalkar\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('sample-pan-card-front.jpg')

# opencv is in BGR and pytesseract only accepts RGB value
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Get text from image
#print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img)) #gives x,y coordinates and diagonal coordinates w,h


"""
Detecting characters
"""
#get height and width of input image
# hImg, Wimg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for box in boxes.splitlines():
#     # print(box)
#     #this generates a list. Now we will split the list for every character
#     box = box.split(' ')
#     print(box)
#     x, y ,w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     #create rectangle around text
#     cv2.rectangle(img, (x,hImg-y), (w, hImg-h), (0,0,255), 3)
#     #put label text around the boxes
#     cv2.putText(img,box[0],(x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


"""
Detecting words
"""
#get height and width of input image
hImg, Wimg, _ = img.shape
boxes = pytesseract.image_to_data(img)
# ignoring first header line of the output
for x, box in enumerate(boxes.splitlines()):
    if x!=0:
        box = box.split()
        print(box)
        if len(box) == 12:
            x, y ,w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            #create rectangle around text
            cv2.rectangle(img, (x,y), (w+x, h+y), (0,0,255), 3)
            #put label text around the boxes
            cv2.putText(img,box[11],(x, y+25), cv2.FONT_ITALIC, 1, (50,50,255), 2)
            




#show pop up of image
cv2.imshow('Result', img)
cv2.waitKey(0)


