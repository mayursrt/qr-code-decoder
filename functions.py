#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
import numpy as np
import cv2
#----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Detect QR Code in the given image
@st.cache
def show_qr_detection(img,pts):
    
    pts = np.int32(pts).reshape(-1, 2)
    
    for j in range(pts.shape[0]):
        
        cv2.line(img, tuple(pts[j]), tuple(pts[(j + 1) % pts.shape[0]]), (255, 0, 0), 5)
        
    for j in range(pts.shape[0]):
        cv2.circle(img, tuple(pts[j]), 10, (255, 0, 255), -1)
#---------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Extract information from the detected QR Code
@st.cache
def qr_code_dec(image):

    decoder = cv2.QRCodeDetector()
    
    data, vertices, rectified_qr_code = decoder.detectAndDecode(image)
    
    if len(data) > 0:
        print("Decoded Data: '{}'".format(data))
    # Show the detection in the image:
        show_qr_detection(image, vertices)
        rectified_image = np.uint8(rectified_qr_code)
        decoded_data = 'Decoded data: '+ data
        rectified_image = cv2.putText(rectified_image,decoded_data,(50,350),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 2,
            color = (250,225,100),thickness =  3, lineType=cv2.LINE_AA)
    return decoded_data
#---------------------------------------------------------------------------------------------------------------------------