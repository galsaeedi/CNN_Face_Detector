
# import the necessary packages
import dlib
import argparse
import cv2

# construct the argument parser and parse the arguments
arg = argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True)
arg.add_argument("-w", "--weights", default='mmod_human_face_detector.dat')
args = vars(arg.parse_args())


# load the input test image and convert it from BGR to RGB
image = cv2.imread(args["image"])
if image is None :
    print("No image !")
    exit()

cnn= dlib.cnn_face_detection_model_v1(args["weights"])

boxes = cnn(image, 1)

############################## drow the rectangle with name in face ##############################
for box in boxes:
    # draw rectangle on faces
    left = box.rect.left()
    top = box.rect.top()
    right = box.rect.right() - left
    bottom = box.rect.bottom() - top
    cv2.rectangle(image, (left,top),(left+right, top+bottom), (0, 255, 0), 2)


# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)