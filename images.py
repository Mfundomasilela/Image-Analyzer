import streamlit as st
import openai
from PIL import Image
import io

# Directly set the API key
api_key = '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'
openai.api_key = api_key

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
    try:
        # Example: Placeholder for actual image processing logic
        response = openai.Image.create(
            file=image_bytes,
            purpose="fine-tune"  # This is just an example, adjust based on actual OpenAI API capabilities
        )
        
        # Display the response
        st.markdown(response['data'])  # Adjust this based on actual response structure

    except Exception as e:
        st.error(f"An error occurred: {e}")
