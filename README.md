# **"Hire Me or Not? Image Classifier Fun"**
**Overview**

Welcome to "Hire Me or Not? Image Classifier Fun" – a whimsical web tool designed to assess job skills through an image classification model. This playful application not only provides skill-based suggestions but also encourages users to share their unique strengths on social media, injecting a fun twist into the conventional job application process.

**Features**

1. Image Classification

The core functionality of the tool involves classifying user-uploaded images related to their skills and work style. This ensures a personalized and entertaining experience for each user.

2. Skill-Based Suggestions
   
Based on the image classification results, the tool provides suggestions for job skills and strengths that the user may possess. This adds a creative and humorous element to the assessment process.

3. Social Media Integration
   
Users are encouraged to share their classification results on various social media platforms, fostering a sense of engagement and networking. Please note that the shareable link feature is currently under development and will be available in future updates.

4. User-Friendly Interface
   
The web tool features an intuitive and user-friendly interface, ensuring accessibility for users of all skill levels. The simplicity of the interface enhances the overall user experience.

**How to Use**

**To utilize the image classification model and interact with the Streamlit app, follow these steps:**

 1. **Download the Streamlit Folder:**
   - Click on the "Download" button or clone the repository to obtain the Streamlit folder.

 2. **Open with Jupyter Notebook or Visual Studio Code:**

   - Depending on your preferred environment, choose one of the following options:
     - **Jupyter Notebook:**
       - Open a Jupyter Notebook.
       - Navigate to the Streamlit folder.
       - Open the `app.py` file.
       - Run the notebook to launch the Streamlit app.

     - **Visual Studio Code:**
       - Open Visual Studio Code.
       - Open the Streamlit folder as your workspace.
       - Locate the `app.py` file.
       - Run the file using the appropriate Visual Studio Code commands.
         
   3. **Loading the Trained Deep Learning Model**

       - Int the app.py file locate the following code snippet:

    ```python
    # Load your trained Inception model outside the main app loop 
    if 'your_image_classifier_module' not in st.session_state:
        model_path = 'C:/Users/susy_/IH-Labs/final-project/Streamlit/models/trained_inception_model.keras'
        st.session_state.your_image_classifier_module = load_model_function(model_path)
    ```

      - Update the `model_path` variable with the path to your trained Inception model file. For example:

    ```python
    # Load your trained Inception model outside the main app loop 
    if 'your_image_classifier_module' not in st.session_state:
        model_path = '/path/to/your/models/trained_inception_model.keras'
        st.session_state.your_image_classifier_module = load_model_function(model_path)
    ```
    Replace `/path/to/your/models/` with the actual path to the folder where you keep the uploaded Streamlit folder and the trained Inception model.

     - Save the changes and run your Streamlit app.
        
**Note**: Keep this file open while using the Streamlit interface.

**To explore the Streamlit visualization, follow these steps:**

  1. **Open Anaconda Command Prompt:**
   - Launch the Anaconda Command Prompt on your system.

  2. **Navigate to the Streamlit Folder:**
   - Use the `cd` command to navigate to the directory where you have downloaded the Streamlit folder.
     "cd /path/to/your/streamlit/folder"

  3. **Run the Streamlit App:**
   - Execute the following command to run the Streamlit app:
     "streamlit run app.py"

Please ensure that you have all the necessary dependencies installed in your Anaconda environment before running the app.

**Note:** If you encounter any issues with running the app, check the console output for error messages, and make sure you have activated the correct Anaconda environment.

Enjoy exploring the image classification model using "Hire Me or Not? Image Classifier Fun"!





































Upload an image related to your skills or work style.
Receive Skill-Based Suggestions:

Explore the humorous and personalized job skill suggestions based on the image classification.
Share Your Results:

Engage with your network by sharing your classification results on social media platforms.
Stay Tuned for Shareable Links:

While the shareable link feature is currently in development, stay tuned for future updates that will allow you to easily share your results.
Technical Details
The image classification is powered by [mention the model or algorithm used].
The user interface is designed using [mention the technology or framework used].
Contributing
We welcome contributions! Feel free to fork the repository, create issues, or submit pull requests.

License
This project is licensed under [mention the license type].
