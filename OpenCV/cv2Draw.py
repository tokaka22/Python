'''
cv2.circle 画圆圈
https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/
'''

import cv2
   
# path
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# Reading an image in default mode
image = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'
  
# Center coordinates
center_coordinates = (120, 50)
 
# Radius of circle
radius = 20
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness) # thickness = -1是实心的
  
# Displaying the image
cv2.imshow(window_name, image)

'''
cv2.putText
'''
cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
            1.0, (0,0,0), thickness = 1) # 照片/添加的文字/左下角坐标/字体/字体大小/颜色/字体粗细

'''
cv2.line
'''
# Python program to explain cv2.line() method 
   
# importing cv2 
import cv2 
   
# path 
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# Reading an image in default mode
image = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'
  
# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)
  
# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (250, 250)
  
# Green color in BGR
color = (0, 255, 0)
  
# Line thickness of 9 px
thickness = 9
  
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv2.line(image, start_point, end_point, color, thickness)
  
# Displaying the image 
cv2.imshow(window_name, image) 