import cv2
import streamlit as st
import numpy as np
from pyzbar.pyzbar import decode

st.title("Webcam Live Feed")
# run = st.checkbox('Run')
FRAME_WINDOW = st.image([])


def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)


run = st.button('Run')
stop = st.button('Stop')
st.write(run,stop)
cap = cv2.VideoCapture(0)
while run:
    ret, frame = cap.read()
    decoder(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')