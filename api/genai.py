import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# Configure the Generative AI model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

# Streamlit app title
st.title("Image Generation with Google Generative AI")

# Upload the sketch image
uploaded_file = st.file_uploader("Upload a sketch image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Sketch", use_column_width=True)

    # Generate the content
    if st.button("Generate Full Diagram"):
        response = model.generate_content(
            ["This is a rough sketch of a drawing. Make the full diagram for this.", img]
        )
        
        # Check if the response contains an image
        if response and 'image' in response:
            generated_image = response['image']
            st.image(generated_image, caption="Generated Diagram", use_column_width=True)
        else:
            st.error("Error generating image. Please try again.")

