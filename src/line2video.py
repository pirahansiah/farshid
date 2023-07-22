import cv2
import numpy as np
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=1
thickness=1
color=(255,255,255)
# Load text file and split into lines
with open('MakeFile', 'r') as f:
    lines = f.read().splitlines() 

# Create blank image 


# Setup video writer
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video = cv2.VideoWriter('text_video.avi', fourcc, 1, (900,900))

# # Add each line to image and write to video
# for line in lines:
#     image = np.zeros((500,500,3), np.uint8)
#     cv2.putText(image, line, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2) 
#     video.write(image)

# video.release()



# line_height = 50 # Height of text line
# text_width = 100
# 
# for line in lines:
#     image = np.zeros((900,900,3), np.uint8) 
#     line_width = cv2.getTextSize(line, font, font_scale, thickness)[0][0]  
    
#     text_height = line_height  
#     while line_width > image.shape[1]:
#         # Text too long to fit on one line
#         subline = line[:image.shape[1]//text_width]  
#         cv2.putText(image, subline, (10,text_height), font, font_scale, color, thickness)
#         video.write(image)
        
#         # Increment text height and remove printed words from line
#         text_height += line_height
#         line = line[image.shape[1]//text_width:]
#         line_width = cv2.getTextSize(line, font, font_scale, thickness)[0][0]
        
#     # Print remaining text normally
#     cv2.putText(image, line, (10,text_height), font, font_scale, color, thickness)
#     video.write(image)

tab_size = 1 # Number of spaces per tab

textHeight = 50 
textX=10
textY=50
image = np.zeros((900,900,3), np.uint8)
for line1 in lines:
    line = line1.expandtabs(tab_size)  
    if textY<800:
        textY=textY+50
    else:
        image = np.zeros((900,900,3), np.uint8)
        textY=50
    # Get width of line with default text size
    (w, h), _ = cv2.getTextSize(line, font, 1, thickness)
    
    # Calculate scale needed to fit line in image width
    scale = image.shape[1] / w
    scale = min(scale, 1.0) # Don't allow scale > 1

    # Get text size and draw 
    textSize = cv2.getTextSize(line, font, scale, thickness)
    textWidth = textSize[0][0]
    cv2.putText(image, line, (10,textY), font, scale, color, thickness)

    # Increment text position
    textHeight += textSize[0][1] 

    video.write(image)

video.release()
