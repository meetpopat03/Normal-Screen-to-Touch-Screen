import numpy as np
import cv2
from collections import deque
import pyautogui

#default called trackbar function 
def setValues(x):
   print("")


# Creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255,setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)

# Creating the trackbars needed for adjusting the marker colour RED COLOR
cv2.namedWindow("Color detectors_click")
cv2.createTrackbar("Upper Hue_click", "Color detectors_click", 10, 180,setValues)
cv2.createTrackbar("Upper Saturation_click", "Color detectors_click", 255, 255,setValues)
cv2.createTrackbar("Upper Value_click", "Color detectors_click", 255, 255,setValues)
cv2.createTrackbar("Lower Hue_click", "Color detectors_click", 0, 180,setValues)
cv2.createTrackbar("Lower Saturation_click", "Color detectors_click", 100, 255,setValues)
cv2.createTrackbar("Lower Value_click", "Color detectors_click", 20, 255,setValues)

# Creating the trackbars needed for adjusting the marker colour GREEN COLOR
cv2.namedWindow("Color detectors_right")
cv2.createTrackbar("Upper Hue_right", "Color detectors_right", 89, 180,setValues)
cv2.createTrackbar("Upper Saturation_right", "Color detectors_right", 255, 255,setValues)
cv2.createTrackbar("Upper Value_right", "Color detectors_right", 255, 255,setValues)
cv2.createTrackbar("Lower Hue_right", "Color detectors_right", 36, 180,setValues)
cv2.createTrackbar("Lower Saturation_right", "Color detectors_right", 50, 255,setValues)
cv2.createTrackbar("Lower Value_right", "Color detectors_right", 70, 255,setValues)

# Creating the trackbars needed for adjusting the marker colour YELLOW COLOR
cv2.namedWindow("Color detectors_double")
cv2.createTrackbar("Upper Hue_double", "Color detectors_double", 35, 180,setValues)
cv2.createTrackbar("Upper Saturation_double", "Color detectors_double", 255, 255,setValues)
cv2.createTrackbar("Upper Value_double", "Color detectors_double", 255, 255,setValues)
cv2.createTrackbar("Lower Hue_double", "Color detectors_double", 25, 180,setValues)
cv2.createTrackbar("Lower Saturation_double", "Color detectors_double", 50, 255,setValues)
cv2.createTrackbar("Lower Value_double", "Color detectors_double", 70, 255,setValues)

#The kernel to be used for dilation purpose 
kernel = np.ones((5,5),np.uint8)
kernel_click = np.ones((5,5),np.uint8)
kernel_right = np.ones((5,5),np.uint8)
kernel_double = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((471,636,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)
paintWindow = cv2.rectangle(paintWindow, (160,1), (255,65), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (275,1), (370,65), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (390,1), (485,65), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (505,1), (600,65), colors[3], -1)

cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)


# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)


# Keep looping
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    #Flipping the frame to see same side of yours
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # For movement
    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue,u_saturation,u_value])
    Lower_hsv = np.array([l_hue,l_saturation,l_value])

    # For Click
    u_hue_click = cv2.getTrackbarPos("Upper Hue_click", "Color detectors_click")
    u_saturation_click = cv2.getTrackbarPos("Upper Saturation_click", "Color detectors_click")
    u_value_click = cv2.getTrackbarPos("Upper Value_click", "Color detectors_click")
    l_hue_click = cv2.getTrackbarPos("Lower Hue_click", "Color detectors_click")
    l_saturation_click = cv2.getTrackbarPos("Lower Saturation_click", "Color detectors_click")
    l_value_click = cv2.getTrackbarPos("Lower Value_click", "Color detectors_click")
    Upper_hsv_click = np.array([u_hue_click,u_saturation_click,u_value_click])
    Lower_hsv_click = np.array([l_hue_click,l_saturation_click,l_value_click])
  
    #for right
    u_hue_right = cv2.getTrackbarPos("Upper Hue_right", "Color detectors_right")
    u_saturation_right = cv2.getTrackbarPos("Upper Saturation_right", "Color detectors_right")
    u_value_right = cv2.getTrackbarPos("Upper Value_right", "Color detectors_right")
    l_hue_right = cv2.getTrackbarPos("Lower Hue_right", "Color detectors_right")
    l_saturation_right = cv2.getTrackbarPos("Lower Saturation_right", "Color detectors_right")
    l_value_right = cv2.getTrackbarPos("Lower Value_right", "Color detectors_right")
    Upper_hsv_right = np.array([u_hue_right,u_saturation_right,u_value_right])
    Lower_hsv_right = np.array([l_hue_right,l_saturation_right,l_value_right])

    #for double
    u_hue_double = cv2.getTrackbarPos("Upper Hue_double", "Color detectors_double")
    u_saturation_double = cv2.getTrackbarPos("Upper Saturation_double", "Color detectors_double")
    u_value_double = cv2.getTrackbarPos("Upper Value_double", "Color detectors_double")
    l_hue_double = cv2.getTrackbarPos("Lower Hue_double", "Color detectors_double")
    l_saturation_double = cv2.getTrackbarPos("Lower Saturation_double", "Color detectors_double")
    l_value_double = cv2.getTrackbarPos("Lower Value_double", "Color detectors_double")
    Upper_hsv_double = np.array([u_hue_double,u_saturation_double,u_value_double])
    Lower_hsv_double = np.array([l_hue_double,l_saturation_double,l_value_double])




    # Adding the colour buttons to the live frame for colour access
    frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
    frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
    frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
    frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
    frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)


    # Identifying the pointer by making its mask
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)

    # Identifying the pointer by making its mask for click
    Mask_click = cv2.inRange(hsv, Lower_hsv_click, Upper_hsv_click)
    Mask_click = cv2.erode(Mask_click, kernel_click, iterations=1)
    Mask_click = cv2.morphologyEx(Mask_click, cv2.MORPH_OPEN, kernel_click)
    Mask_click = cv2.dilate(Mask_click, kernel_click, iterations=1)

    Mask_right = cv2.inRange(hsv, Lower_hsv_right, Upper_hsv_right)
    Mask_right = cv2.erode(Mask_right, kernel_right, iterations=1)
    Mask_right = cv2.morphologyEx(Mask_right, cv2.MORPH_OPEN, kernel_right)
    Mask_right = cv2.dilate(Mask_right, kernel_right, iterations=1)

    Mask_double = cv2.inRange(hsv, Lower_hsv_double, Upper_hsv_double)
    Mask_double = cv2.erode(Mask_double, kernel_double, iterations=1)
    Mask_double = cv2.morphologyEx(Mask_double, cv2.MORPH_OPEN, kernel_double)
    Mask_double = cv2.dilate(Mask_double, kernel_double, iterations=1)

    # Find contours for the pointer after idetifying it
    cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    center = None

    # Find contours for the pointer after idetifying it for click
    cnts_click,_ = cv2.findContours(Mask_click.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    center_click = None

    cnts_right,_ = cv2.findContours(Mask_right.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    center_right = None

    cnts_double,_ = cv2.findContours(Mask_double.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    center_double = None


    # Ifthe contours are formed
    if len(cnts) > 0:
    	# sorting the contours to find biggest 
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
        pyautogui.moveTo(center[0]*2, center[1]*2)
        
    # Ifthe contours are formed
    elif len(cnts_click) > 0:
    	# sorting the contours to find biggest 
        cnt_click = sorted(cnts_click, key = cv2.contourArea, reverse = True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt_click)
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt_click)
        center_click = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
        pyautogui.click(center_click[0]*2, center_click[1]*2)

    # elif len(cnts_right) > 0:
    # 	# sorting the contours to find biggest 
    #     cnt = sorted(cnts_right, key = cv2.contourArea, reverse = True)[0]
    #     # Get the radius of the enclosing circle around the found contour
    #     ((x, y), radius) = cv2.minEnclosingCircle(cnt)
    #     # Draw the circle around the contour
    #     cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    #     # Calculating the center of the detected contour
    #     M = cv2.moments(cnt)
    #     center_right = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

    #     pyautogui.rightClick(center_right[0], center_right[1])

    # elif len(cnts_double) > 0:
    # 	# sorting the contours to find biggest 
    #     cnt = sorted(cnts_double, key = cv2.contourArea, reverse = True)[0]
    #     # Get the radius of the enclosing circle around the found contour
    #     ((x, y), radius) = cv2.minEnclosingCircle(cnt)
    #     # Draw the circle around the contour
    #     cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    #     # Calculating the center of the detected contour
    #     M = cv2.moments(cnt)
    #     center_double = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

    #     pyautogui.doubleClick(center_double[0], center_double[1])

    # Draw lines of all the colors on the canvas and frame 

    # Show all the windows
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paintWindow)
    cv2.imshow("mask",Mask)

	# If the 'q' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and all resources
cap.release()
cv2.destroyAllWindows()



# # Specify the pixel coordinates where you want to click
# x_coordinate = 873  # Replace with your desired x-coordinate
# y_coordinate = 1049  # Replace with your desired y-coordinate

# # Perform a left mouse click at the specified coordinates
# pyautogui.click(x_coordinate, y_coordinate)

# def fun(x,y):
#     pyautogui.click(x, y)

# def pixel_value(): # x=center[0], y=center[1]
#     # Reading the frame from the camera
#     frame = cap.read()
#     #Flipping the frame to see same side of yours
#     frame = cv2.flip(frame, 1)
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
#     u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
#     u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
#     l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
#     l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
#     l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
#     Upper_hsv = np.array([u_hue,u_saturation,u_value])
#     Lower_hsv = np.array([l_hue,l_saturation,l_value])

#     # Identifying the pointer by making its mask
#     Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
#     Mask = cv2.erode(Mask, kernel, iterations=1)
#     Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
#     Mask = cv2.dilate(Mask, kernel, iterations=1)

#     # Find contours for the pointer after idetifying it
#     cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
#     	cv2.CHAIN_APPROX_SIMPLE)
#     center = None

#     # Ifthe contours are formed
#     if len(cnts) > 0:
#     	# sorting the contours to find biggest 
#         cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
#         # Get the radius of the enclosing circle around the found contour
#         ((x, y), radius) = cv2.minEnclosingCircle(cnt)
#         # Draw the circle around the contour
#         cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
#         # Calculating the center of the detected contour
#         M = cv2.moments(cnt)
#         center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
#         fun(center[0],center[1])
#     return center

# while True :
#     pixel_value()