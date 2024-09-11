import streamlit as st
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv
import base64
from io import BytesIO
from PIL import Image

# Load environment variables
load_dotenv()

# Configure API tokens
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
api_key = os.getenv('GEMINI_API_KEY')

# Configure the Gemini API using the loaded key
genai.configure(api_key=api_key)

# Initialize the Gemini text model
text_model = genai.GenerativeModel('gemini-pro')

# Hugging Face API endpoints
IMAGE_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# Query Hugging Face image generation model
def query_image_model(payload):
    try:
        response = requests.post(IMAGE_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content  # Return image bytes if successful
    except requests.exceptions.RequestException as e:
        st.error(f"Image generation error: {e}")
        return None

# Generate story using Gemini model
def generate_story(prompt):
    try:
        response = text_model.generate_content(f"Write a short children's story about {prompt} in 5 brief paragraphs.")
        story = response.text.split('\n\n')
        return story[:5]  # Ensure we have exactly 5 paragraphs
    except Exception as e:
        st.error(f"Error generating story: {e}")
        return None

# Generate image using Hugging Face API
def generate_image(prompt):
    image_bytes = query_image_model({"inputs": prompt})
    if image_bytes:
        try:
            image = Image.open(BytesIO(image_bytes))
            # Resize the image to a standard size for consistency
            image = image.resize((400, 300))  # Standard size: 400x300
            return image
        except Exception as e:
            st.error(f"Error processing image: {e}")
            return None
    else:
        return None

# Streamlit interface
st.title("Children's Story Generator 📖✨")

story_name = st.text_input("Enter a name or theme for the story:")

# Button to generate story and images
if st.button("Generate Story"):
    if story_name:
        with st.spinner("Generating story and images..."):
            story_chunks = generate_story(story_name)
            if story_chunks:
                images = [generate_image(chunk) for chunk in story_chunks]
                
                st.subheader(f"Story: {story_name}")
                
                story_text = ""
                
                # Display each paragraph with its image
                for i, (paragraph, image) in enumerate(zip(story_chunks, images)):
                    story_text += f"{i+1}. {paragraph}\n\n"
                    cols = st.columns(2)
                    with cols[0]:
                        st.markdown(f"**{i+1}.** {paragraph}")
                    with cols[1]:
                        if image:
                            st.image(image, use_column_width=True)
                        else:
                            st.write("Image generation failed")
                
                # Add a copy to clipboard button
                st.markdown("### Copy the entire story:")
                st.text_area("", story_text, height=150)
                st.code(f"Story:\n{story_text}")
                if st.button("Copy Story"):
                    st.success("Story copied to clipboard!")

            else:
                st.error("Story generation failed.")
    else:
        st.warning("Please enter a name or theme for the story.")

# Custom CSS for better UI
st.markdown("""
    <style>
        .stImage > img {
            width: 100%;
            max-height: 300px;
            object-fit: contain;
            border: 2px solid #4CAF50;
            border-radius: 10px;
        }
        .stTextArea {
            background-color: #f1f1f1;
            border-radius: 10px;
        }
        button[aria-label="Copy Story"] {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
