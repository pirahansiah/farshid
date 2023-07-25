
import cv2
import numpy as np
import os
import glob
w=3840
h=2160
def resize_with_aspect_ratio(image, new_width, new_height):
    cropped_images = []
    height, width = image.shape[:2]    
    crop_x = (width - new_width) // 2
    crop_y = (height - new_height) // 2
    for i in range(height // new_height):
        for j in range(width // new_width):
            x = crop_x + j * new_width
            y = crop_y + i * new_height
            cropped_image = image[y:y+new_height, x:x+new_width]
            cropped_images.append(cropped_image)
            #cv2.imshow("test",cropped_image)
            #cv2.waitKey(200)    
    return cropped_images

def copyBig(small,big):
    center_y = big.shape[0]//2
    center_x = big.shape[1]//2
    h, w = small.shape[:2]
    roi_top = center_y - h//2
    roi_bottom = roi_top + h
    roi_left = center_x - w//2
    roi_right = roi_left + w
    roi = big[roi_top:roi_bottom, roi_left:roi_right]
    img1_resized = cv2.resize(small, (w, h)) 
    np.copyto(roi, img1_resized)
    # cv2.imshow("test",big)
    # cv2.waitKey(200)
    return big
cropped_images=[]
img_array = []
for filepath in glob.glob('images/*.png'):
    img = cv2.imread(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    img=cv2.resize(img,(w,h))
    #img=resize_with_aspect_ratio(img,w,h)
    img_array.append((filename[3:], img))
   
out = cv2.VideoWriter('MindMaps.mp4',cv2.VideoWriter_fourcc(*'FMP4'), 1, (w,h))


# for j in range(len(img_array)): 
#     for i in range(calcFrames*5):
#         out.write(img_array[j])


# for j in range(len(qrcode_array)): 
#     for i in range(calcFrames):
#         out.write(qrcode_array[j])
# out.release()


for filename, frame in img_array:
    canvas = cv2.copyMakeBorder(frame, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))  # Add space for the caption
    caption = f' {filename}'
    cv2.putText(canvas, caption, (10, frame.shape[0] + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255, 255), 2, cv2.LINE_AA)
    canvas=cv2.resize(canvas,( w,h))
    for _ in range(10):
        out.write(canvas)
out.release()