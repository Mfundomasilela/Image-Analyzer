from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os
from PIL import Image
import io

# Load environment variables
load_dotenv()
MODEL = 'gpt-4'  
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.title('AI IMAGE ANALYZER')

# Upload image file
image_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

if image_file:
    # Display image
    image = Image.open(image_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=image.format)
    image_bytes.seek(0)

    # Analyze image 
    response = client.images.analysis.create(
        model="pexels-thatguycraig000-1563356.jpg",  
        file=image_bytes,
    )

    # Display the response
    st.markdown(response.choices[0].message.content)
