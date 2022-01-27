import cv2

#Initialize classifier object
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#load image
#img = cv2.imread("photo.jpg")
#or take picture of user
video = cv2.VideoCapture(0) #add index of whichever camera you want to use
refFrame = None

count = 0

while count < 40:
    check, frame = video.read()
    #convert to grayscale
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #update reference frame until reference frame is 40th frame, then don't change
    refFrame = frame
    count += 1

cv2.imshow("Face Detector", refFrame)

#Create greyscale copy
grayImg = cv2.cvtColor(refFrame, cv2.COLOR_BGR2GRAY)

#faces is an array representing rectangle that captures faces [xth pixel, yth pixel, length, width]
#faces will be an array of arrays if multiple faces are detected
faces = faceCascade.detectMultiScale(grayImg, scaleFactor = 1.13, minNeighbors = 3)

#loop to draw a rectangle around detected faces
for x, y, w, h in faces:
                      #image  #top left corner   #bottom right corner   #color    #line width
    refFrame = cv2.rectangle(refFrame,       (x,y),       (x + w, y + h),        (0, 255, 0),     3)

print(type(faces))
print(faces)  

#eyeCascade = cv2.CascadeClassifier("eyes.xml")
#eyes = eyeCascade.detectMultiScale(grayImg, scaleFactor = 1.05, minNeighbors = 5)
#for x, y, w, h in eyes:
    #img = cv2.rectangle(refFrame, (x,y), (x + w, y + h), (255, 0, 0), (3))

#print("Eyes Detected: \n", eyes)
cv2.imshow("Face Detector", refFrame)
cv2.waitKey(0)
cv2.destroyAllWindows()