import cv2
import numpy as np

class Thresholding:
    def __init__(self, grayImg):
        self.grayImg = grayImg

    def manually_python(self):        
        threshval = 128
        binaryImg = np.where(self.grayImg < threshval, self.grayImg, 0) if threshval < 128 else np.where(self.grayImg > threshval, self.grayImg, 0)
        return binaryImg
    
    def manually(self,threshval):        
        binaryImg = np.zeros_like(self.grayImg)
        for i in range(self.grayImg.shape[0]): #height 
            for j in range(self.grayImg.shape[1]): #width 
                if self.grayImg[i, j] < threshval:
                    binaryImg[i, j] = 0 
                else:
                    binaryImg[i, j] = 1 
        return binaryImg    

    def pirahansiah_threshold_method_find_threshold_values_2(self):
        #http://www.jatit.org/volumes/Vol95No21/1Vol95No21.pdf
        #https://pdfs.semanticscholar.org/05b2/d39fce4e8a99897e95f8c75416f65a5a0acc.pdf
        assert self.grayImg is not None, "file could not be read, check with os.path.exists()"
        #img = cv2.GaussianBlur(self.grayImg, (3, 3), 0)       
        img = self.grayImg
        # Initialize an array to store the PSNR values for each threshold value
        psnr_values = np.zeros(256)        
        psnr_max=0
        th=0
        # Iterate over all possible threshold values with a step size of 5
        for t in range(0, 256, 5):
            # Threshold the image using the current threshold value
            _, binary = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)            
            # Calculate the PSNR between the binary image and the original image
            psnr = cv2.PSNR(binary, img)            
            # Store the PSNR value
            psnr_values[t] = psnr
            if (psnr_max<psnr):
                psnr_max=psnr
                th=t        
        # Calculate the mean PSNR value
        mean_psnr = np.mean(psnr_values)
        th=int(th/mean_psnr)
        # Find the threshold values that satisfy the condition
        thresh = th #np.argwhere((mean_psnr / k1 < psnr_values) & (psnr_values < mean_psnr / k2)).flatten()
        
        return thresh
    def pirahansiah_threshold_method_find_threshold_values_1(self):      
        #https://www.jatit.org/volumes/Vol57No2/4Vol57No2.pdf                      
        assert self.grayImg is not None, "file could not be read, check with os.path.exists()"
        gray = cv2.GaussianBlur(self.grayImg, (3, 3), 0)                
        max1=0
        max2=0     
        # Iterate over all possible threshold values
        for t in range(0, 256, 10):            
            # Threshold the image using the current threshold value            
            _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)          
            # Find the contours in the binary image            
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)                             
            if max1<=len(contours):
                max1=len(contours)
                max2=t                        
        threshold_values =max2 
        return threshold_values


    def opencv_th(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color = (0, 0, 0)
        colorInv = (255, 255, 255)
        thickness = 2
        # Set the position of the text
        textX = 25
        textY = 45
        textSize, _ = cv2.getTextSize("Otsu Method   ", font, fontScale, thickness)
        # Draw a white rectangle behind the text
        
        # Apply different thresholding methods
        _, binaryImg = cv2.threshold(self.grayImg, 128, 255, cv2.THRESH_BINARY)                
        cv2.rectangle(binaryImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(binaryImg, 'Binary', (textX, textY), font, fontScale, color, thickness)
        
        _, binaryInvImg = cv2.threshold(self.grayImg, 128, 255, cv2.THRESH_BINARY_INV)
        cv2.rectangle(binaryInvImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(binaryInvImg, 'Binary Inv', (textX, textY), font, fontScale, color, thickness)
        
        _, truncImg = cv2.threshold(self.grayImg, 128, 255, cv2.THRESH_TRUNC)
        cv2.rectangle(truncImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(truncImg, 'Trunc', (textX, textY), font, fontScale, color, thickness)
        
        _, toZeroImg = cv2.threshold(self.grayImg, 128, 255, cv2.THRESH_TOZERO)
        cv2.rectangle(toZeroImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(toZeroImg, 'To Zero', (textX, textY), font, fontScale, color, thickness)
        
        _, toZeroInvImg = cv2.threshold(self.grayImg, 128, 255, cv2.THRESH_TOZERO_INV)
        cv2.rectangle(toZeroInvImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(toZeroInvImg, 'To Zero Inv', (textX, textY), font, fontScale, color, thickness)
        
        adaptiveImg = cv2.adaptiveThreshold(self.grayImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.rectangle(adaptiveImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(adaptiveImg, 'Adaptive', (textX, textY), font, fontScale, color, thickness)
        
        otsu_threshold, image_result = cv2.threshold(self.grayImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)        
        cv2.rectangle(image_result, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(image_result, 'Otsu Threshold Method', (textX, textY), font, fontScale, color, thickness)

        threshval=self.pirahansiah_threshold_method_find_threshold_values_1()        
        th_img = th.manually(threshval)
        binaryImg = th_img * 255
        cv2.rectangle(binaryImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(binaryImg, 'PirahanSiah Threshold ', (textX, textY), font, fontScale, color, thickness)


        cv2.rectangle(self.grayImg, (textX, textY - textSize[1]), (textX + textSize[0], textY), (255, 255, 255), -1)
        cv2.putText(self.grayImg, 'Original', (textX, textY), font, fontScale, color, thickness)
        # Concatenate the images into a grid with 3 rows and 3 columns
        row1 = np.concatenate((self.grayImg, binaryImg, binaryInvImg), axis=1)
        row2 = np.concatenate((truncImg, toZeroImg, toZeroInvImg), axis=1)                
        row3 = np.concatenate((adaptiveImg, image_result, binaryImg), axis=1) # np.zeros_like(adaptiveImg)
        concatenatedImg = np.concatenate((row1, row2, row3), axis=0)            
        # Resize the concatenated image to fit the screen resolution
        screenRes = (1920-200, 1080-200)
        scaleWidth = screenRes[0] / concatenatedImg.shape[1]
        scaleHeight = screenRes[1] / concatenatedImg.shape[0]
        scale = min(scaleWidth, scaleHeight)
        windowWidth = int(concatenatedImg.shape[1] * scale)
        windowHeight = int(concatenatedImg.shape[0] * scale)
        resizedImg = cv2.resize(concatenatedImg, (windowWidth, windowHeight))
        # Display the resized image
        cv2.imshow('Thresholded Images', resizedImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":    
    img = cv2.imread("opencv.png")    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    th = Thresholding(gray)    
    th.opencv_th()

    #threshval = 128
    # read an image
    # convert it to grayscale
    #threshval=th.pirahansiah_threshold_method_find_threshold_values_1()
    # threshval=th.pirahansiah_threshold_method_find_threshold_values_2()        
    # th_img = th.manually(threshval)
    # binaryImg = th_img * 255
    # cv2.imshow('image', binaryImg)
    # cv2.waitKey(100)


'''
cv::Mat binaryImg = threshval < 128 ? (grayImg < threshval) : (grayImg > threshval);
#thresholding #opencv #python

The PirahanSiah’s method for thresholding, described in the paper, uses a gray-scale histogram, 
thresholding range, and the Peak Signal-to-Noise Ratio (PSNR) to segment images and find the best 
threshold values to binarize the image. They argue that thresholding is an important problem in 
pattern recognition and use the PSNR quality measure to assess the similarities between the 
original and binarized image. They calculate PSNRs for every threshold value and use the 
difference between the PSNR of the previous threshold image and the new one to select the 
threshold value. They also describe a multi-threshold algorithm that applies multiple 
threshold values and computes the total number of blobs or objects in an image for each threshold.
The peak threshold values are those with the highest total number of blobs compared to their threshold neighbors.
In addition, their method uses thresholding on images suitable for OCR systems, LPR systems, etc.

The proposed adaptive threshold method, based on the Peak Signal-to-Noise Ratio (PSNR), 
has the potential to be applied in all domains, such as LPR and OCR. The proposed algorithm 
achieves competitive results in four databases, including Malaysian vehicle, standard, 
printed and handwritten images. The objective of this research was to develop a new single 
adaptive thresholding algorithm that works for a wide range of pattern recognition applications. 
The proposed method has been implemented in four different types of applications and compared 
with other methods. The results show that the proposed algorithm achieves the objective because 
it has obtained reasonable results in all four areas/domains.
https://www.jatit.org/volumes/Vol57No2/4Vol57No2.pdf 
http://www.jatit.org/volumes/Vol95No21/1Vol95No21.pdf
https://pdfs.semanticscholar.org/05b2/d39fce4e8a99897e95f8c75416f65a5a0acc.pdf
'''