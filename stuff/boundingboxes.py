import cv2
import numpy as np

def bboxes(results,classes,frame):
    #makes a copy of the frame 
    img = frame 

    #Function to draw frame on people using the coordinates appended
    #loop over the results
    for (index,(classid,prob,bbox,centeriod)) in enumerate(results):

        #filters the function for people detection 
        if classid == 0:

            #extract the bounding box and centroid coordinates 
            (startx,starty,endx,endy) = bbox

            #setup the color of the annotation
            color = (0,255,0)

            #grabbing the centroid 
            (cx,cy) = centeriod

            #grabbing the class name of the prediction 
            label = str(classes[classid])

            #draw a bounding box around the detected objects
            cv2.rectangle(img,(startx,starty),(endx,endy),color,2)

            #draw circle around centroid coordinates of the person
            cv2.circle(img,(cx,cy),5,color,1)

    return img