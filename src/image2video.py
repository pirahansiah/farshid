
import cv2
import numpy as np
import os
import glob
w=3840
h=2160
time_video_min=0.5
calcFrames=int(time_video_min*60*15)
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
for filename in glob.glob('images/*.png'):
    img = cv2.imread(filename)
    img=cv2.resize(img,(w,h))
    img_array.append(img)
   
qrcode_array = []
files_qrcode=glob.glob('qrcode/*.png')
sorted_file_paths = sorted(files_qrcode)
for filepath in sorted_file_paths: #glob.glob('qrcode/*.png'):
    big_image=np.zeros(( h,w, 3),dtype=np.uint8) # np is not opencv the h,w is w,h
    img = cv2.imread(filepath)
    #filename = os.path.basename(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    img=cv2.resize(img,( 600,600))
    #big_image=copyBig(img,big_image)
    #qrcode_array.append(img)    
    qrcode_array.append((filename[3:], img))

out = cv2.VideoWriter('qrCode.mp4',cv2.VideoWriter_fourcc(*'FMP4'), 15,(800,900)) # (w,h))


# for j in range(len(img_array)): 
#     for i in range(calcFrames*5):
#         out.write(img_array[j])


# for j in range(len(qrcode_array)): 
#     for i in range(calcFrames):
#         out.write(qrcode_array[j])
# out.release()


for filename, frame in qrcode_array:
    # Add the filename as a caption
    #caption = f'File: {filename}'
    #cv2.putText(frame, caption, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    canvas = cv2.copyMakeBorder(frame, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))  # Add space for the caption

    # Add the filename as a caption
    caption = f' {filename}'
    cv2.putText(canvas, caption, (10, frame.shape[0] + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255, 255), 2, cv2.LINE_AA)

    canvas=cv2.resize(canvas,( 800,900))
    # Repeat the frame multiple times
    for _ in range(calcFrames):
        out.write(canvas)


'''
How to create a video with images in Python using OpenCV library
The OpenCV library is a powerful tool for computer vision. 
It can be used to create videos with images, and other types of media.
This code creates a video with images. The images are resized to 3840x2160 pixels.
The video is encoded with the FMP4 codec and has a frame rate of 15 frames per second.

    # if 1: #img.shape[0]>w or img.shap[0]>h:
    #     print ("not good")
    #     new_width=600 #img.shap[0]
    #     new_height=600
    #     cropped_images = resize_with_aspect_ratio(img, new_width, new_height)
    #     # Save the cropped images
    #     for i, cropped_image in enumerate(cropped_images):
    #         #cv2.imwrite(f'cropped_image_{i}.jpg', cropped_image)
    #         cropped_image=cv2.resize(cropped_image,(w,h))
    #         img_array.append(cropped_image)


'''