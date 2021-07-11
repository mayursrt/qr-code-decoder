#----------------------------------------------------------------------------------------------------------------------------
# Imports
import streamlit as st
from PIL import Image
import numpy as np
import cv2
# from qrtools.qrtools import QR
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

with st.form(key='my_form', clear_on_submit=False):
    qr_image = st.file_uploader("Upload a QR Code", type=['png','jpeg','jpg'])
    st.text('Note : Prefer to upload a QR Code image')
    submit_button = st.form_submit_button(label='Decode')

#----------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------
# Main Function
# @st.cache
def show_qr_detection(img,pts):
    
    pts = np.int32(pts).reshape(-1, 2)
    
    for j in range(pts.shape[0]):
        
        cv2.line(img, tuple(pts[j]), tuple(pts[(j + 1) % pts.shape[0]]), (255, 0, 0), 5)
        
    for j in range(pts.shape[0]):
        cv2.circle(img, tuple(pts[j]), 10, (255, 0, 255), -1)


# @st.cache
def qr_code_dec(image):

    decoder = cv2.QRCodeDetector()
    
    data, vertices, rectified_qr_code = decoder.detectAndDecode(image)
    
    if len(data) > 0:
        print("Decoded Data: '{}'".format(data))

    # Show the detection in the image:
        show_qr_detection(image, vertices)
        
        rectified_image = np.uint8(rectified_qr_code)
        
        decoded_data = data
        
        rectified_image = cv2.putText(rectified_image,decoded_data,(50,350),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 2,
            color = (250,225,100),thickness =  3, lineType=cv2.LINE_AA)
        
        
    return decoded_data
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
# Body



ph = st.empty()
col1, col2, col3 = st.beta_columns([5,10,5])

if qr_image:
    ph.markdown("<h2 style='text-align: center; color: black;'>Uploaded Image/QR Code</h1>", unsafe_allow_html=True)
    qr_image = np.array(Image.open(qr_image))
    decoded_qr_data = qr_code_dec(qr_image)
    col2.image(qr_image, use_column_width=True)
    st.markdown(f"<h3 style='text-align: center; color: black;'>Decoded Data : {decoded_qr_data}</h1>", unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------
# Footer

#MainMenu {visibility: hidden;}
footer="""<style>


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



############################################################################################################################# 
#############################################################################################################################
