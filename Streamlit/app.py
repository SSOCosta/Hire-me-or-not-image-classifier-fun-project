from pathlib import Path
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from google.cloud import storage
import io
import os

#Generating a temporary directory for storage in google cloud
if not os.path.exists('/tmp/'):
    os.makedirs('/tmp/')

# Loading the model from Google Cloud Storage

bucket_name = 'hire-me-or-not-imageclassifier'
model_blob_name = 'Hire-me-or-not-imageclassifier/Streamlit/models/trained_inception_model.keras'

def load_model_from_gcs(bucket_name, model_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(model_blob_name)
    model_path = "/tmp/model.keras"  
    blob.download_to_filename(model_path)
    return load_model(model_path)


if 'your_image_classifier_module' not in st.session_state:
    st.session_state.your_image_classifier_module = load_model_from_gcs(bucket_name, model_blob_name)

# Confidence threshold to consider an identification
confidence_threshold = 0.4

# Define the get_description function
def get_description(label):
    if label == "The Multitasking Maestro":
        return (
            "Individuals in this category excel at juggling multiple tasks simultaneously. "
            "Whether it's answering emails, conducting meetings, or wrangling spreadsheets, they're the masters of multitasking.\n"
            "\n"
            "Connection to Job Skills: Highlights skills related to time management, organization, and adaptability.\n\n"
        )
    elif label == "The Code Sorcerer":
        return (
            "Wizards of the coding world, these individuals bring a touch of magic to programming. "
            "Their spells are written in code, and debugging is their mystical art.\n"
            "\n"
            "Connection to Job Skills: Emphasizes programming and problem-solving skills.\n\n"
        )
    # Add descriptions for the remaining categories in a similar manner
    elif label == "The Creative Alchemist":
        return (
            "Turning imagination into reality, these alchemists craft ideas into beautiful creations. "
            "From graphic design to storytelling, they bring a touch of magic to the creative process.\n"
            "\n"
            "Connection to Job Skills: Highlights creativity, design, and storytelling abilities.\n\n"
        )
    elif label == "The Team Harmony Composer":
        return (
            "Masters of team dynamics, these individuals conduct the symphony of collaboration. "
            "They ensure that every member plays their part, creating a harmonious work environment.\n"
            "\n"
            "Connection to Job Skills: Emphasizes teamwork, communication, and leadership skills.\n\n"
        )
    elif label == "The Data Whisperer":
        return (
            "In the realm of data, these individuals possess an innate ability to decipher patterns and glean insights. "
            "They whisper to the data, and it reveals its secrets.\n"
            "\n"
            "Connection to Job Skills: Highlights data analysis and problem-solving skills.\n\n"
        )
    elif label == "The Time Traveling Trendsetter":
        return (
            "Breaking the barriers of time, these trendsetters stay ahead of the curve. "
            "From futuristic fashion to cutting-edge tech, they're the visionaries of their time.\n"
            "\n"
            "Connection to Job Skills: Emphasizes innovation, adaptability, and staying current with industry trends.\n\n"
        )
    elif label == "The Growth Hacking Magician":
        return (
            "Magicians in the world of growth hacking, these individuals conjure strategies to propel businesses forward. "
            "Their tricks involve turning challenges into opportunities.\n"
            "\n"
            "Connection to Job Skills: Highlights strategic thinking, problem-solving, and marketing skills.\n\n"
        )
    elif label == "The Communication Jedi":
        return (
            "Masters of the art of communication, these Jedi navigate the language galaxy with ease. "
            "From writing to public speaking, they wield words like lightsabers.\n"
            "\n"
            "Connection to Job Skills: Emphasizes communication, writing, and presentation skills.\n\n"
        )
    elif label == "The Serendipity Explorer":
        return (
            "Navigating the unexpected with grace, these explorers thrive in uncertainty. "
            "They turn serendipity into opportunity, discovering hidden gems along the way.\n"
            "\n"
            "Connection to Job Skills: Highlights adaptability, resilience, and a positive attitude.\n\n"
        )
    elif label == "The Quantum Leap Dreamer":
        return (
            "Dreamers who make quantum leaps toward their goals, these individuals have their sights set on the stars. "
            "They believe that anything is possible with a dash of ambition.\n"
            "\n"
            "Connection to Job Skills: Emphasizes ambition, goal-setting, and a forward-thinking mindset.\n\n"
        )
    else:
        return "No specific description available for this category."

# Front page content
image_path = "Streamlit/images/1655272458248.jpg"
image = Image.open(image_path)
st.image(image, use_column_width=True)
st.title("Hire Me or Not? Image Classifier Fun")
st.write(
        "Upload an image that captures your work life and unlock humorous classifications based on your professional skills. Let's add a touch of fun to your unique talents!"
    )    
    
# Rest of the Streamlit app code
uploaded_image = st.file_uploader(
    "Upload your image here:",
    type=('png', 'jpg', 'jpeg', 'gif', 'bmp')
)

# Define your labels/categories based on your model
labels = ["The Multitasking Maestro", "The Code Sorcerer", "The Creative Alchemist", "The Team Harmony Composer", "The Data Whisperer", "The Time Traveling Trendsetter", "The Growth Hacking Magician", "The Communication Jedi",
          "The Serendipity Explorer", "The Quantum Leap Dreamer"]

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, use_column_width=True)

    # Resize and preprocess the image for the model
    target_size = (256, 256)
    image = image.resize(target_size)
    image_array = keras_image.img_to_array(image.convert('RGB'))  # Convert to RGB
    image_array = preprocess_input(np.expand_dims(image_array, axis=0))

    # Use your image classifier to get predictions
    predictions = st.session_state.your_image_classifier_module.predict(image_array)[0]

    # Display the highest confidence classification above the threshold
    max_confidence_idx = np.argmax(predictions)
    max_confidence_value = predictions[max_confidence_idx]

    if max_confidence_value >= confidence_threshold:
        max_confidence_label = labels[max_confidence_idx]

        # Display the result
        st.subheader("Classification Results:")
        st.write(f"{max_confidence_label}: {max_confidence_value * 100:.2f}%")

        # Display the corresponding description
        description = get_description(max_confidence_label)
        st.subheader("Description:")
        st.write(description)
        
        # Shareable link
        share_link = f"Share your results on LinkedIn: [Click here](http://yourdomain.com/share/{max_confidence_label})"
        st.subheader("Share Your Results:")
        st.markdown(share_link, unsafe_allow_html=True)
    else:
        # Display a message when confidence is below the threshold
        st.subheader("Whispers of Uncertainty")
        st.write("The model seems to be on a vacation from confidence and is enjoying the uncertainty of the moment.\n Please upload another image.")