#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from PIL import Image
import numpy as np
from pyzbar.pyzbar import decode
from functions import *
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Title and Logo
title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 5])
image = Image.open('assets/logo.jpg')
with title_container:
    with col1:
       st.image(image)
    with col2:
        st.title('QR Code Decoder')
        st.markdown("""
Decode QR Codes on the go.
""")
st.write('')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# User Input
qr_image = st.file_uploader("Upload a QR Code", type=['png','jpeg','jpg'])
st.text('Note : Prefer to upload a QR Code image')
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Body
if qr_image:
    try:
        ph = st.empty()
        col1, col2, col3 = st.beta_columns([5,10,5])
        ph.markdown("<h2 style='text-align: center; color: black;'>Uploaded Image/QR Code</h1>", unsafe_allow_html=True)
        qr_image = np.array(Image.open(qr_image))
        decoded_qr_data = qr_code_dec(qr_image)
        col2.image(qr_image, use_column_width=True)
        st.markdown(f"<h3 style='text-align: center; color: black;'>{decoded_qr_data}</h1>", unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"<p style='text-align: center; color: red;'>Cannot extract information from the uploaded image, Please upload a valid QR Code image</p>", unsafe_allow_html=True)
#----------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------
# Links
st.write('')
st.markdown(f"<p style='text-align: center; color: black;'>To generate a QR Code from a link or any text, visit this <a href='https://qr-code-generat0r.herokuapp.com/'>QR Code Generator.</a></p>.", unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



# ############################################################################################################################# 
# st.title("Webcam Live Feed")
# # run = st.checkbox('Run')
# FRAME_WINDOW = st.image([])


# def decoder(image):
#     gray_img = cv2.cvtColor(image,0)
#     barcode = decode(gray_img)

#     for obj in barcode:
#         points = obj.polygon
#         (x,y,w,h) = obj.rect
#         pts = np.array(points, np.int32)
#         pts = pts.reshape((-1, 1, 2))
#         cv2.polylines(image, [pts], True, (0, 255, 0), 3)

#         barcodeData = obj.data.decode("utf-8")
#         barcodeType = obj.type
#         string = "Data: " + str(barcodeData) + " | Type: " + str(barcodeType)
        
#         cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255), 2)
#         print("Barcode: "+barcodeData +" | Type: "+barcodeType)


# run = st.button('Run')
# stop = st.button('Stop')
# st.write(run,stop)
# cap = cv2.VideoCapture(0)
# while run:
#     ret, frame = cap.read()
#     decoder(frame)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     FRAME_WINDOW.image(frame)
# else:
#     st.write('Stopped')

# #############################################################################################################################



#---------------------------------------------------------------------------------------------------------------------------
# Footer
footer="""<style>

#MainMenu {visibility: hidden;}
a:link , a:visited{
color: black;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made in Streamlit with ❤️ by <a href='https://github.com/mayursrt'>Mayur</a>.

</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------



