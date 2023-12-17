# **"Hire Me or Not? Image Classifier Fun"**
## Overview

Welcome to "Hire Me or Not? Image Classifier Fun" – a whimsical web tool designed to assess job skills through an image classification model. This playful application not only provides skill-based suggestions but also encourages users to share their unique strengths on social media, injecting a fun twist into the conventional job application process.

## Code

### Programming Language:

- Python

### Dependencies (Libraries):

- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical operations on arrays.
- **Matplotlib and Seaborn:** Data visualization.
- **TensorFlow:** Deep learning library for the machine learning model.
- **Scikit-Learn:** Machine learning tools, including train-test split and recall_score.
- **Keras:** High-level neural networks API.
- **Pickel:** Serialization and deserialization of Python objects.
- **OS and shutil:** Operating system and file operations.
- **Random:** Random number generation for data splitting.
- **Image Data Generator:** Part of TensorFlow for image preprocessing.
- **InceptionV3:** Pre-trained deep learning model from TensorFlow.

## Skills Presentation

The foundation of this project revolves around the pivotal role that skills play in the hiring process. A dedicated presentation was conducted to underscore the significance of skills in shaping successful careers and fostering professional growth.

### Exploring Skill Importance

The presentation delved into the critical importance of skills when evaluating and hiring individuals for various roles. Key points covered include:

- Type of skills: soft skills vs hard skills.
- European Countries skill rank index, available at https://www.cedefop.europa.eu/en/tools/european-skills-index
- How possessing a diverse skill set enhances adaptability and problem-solving capabilities.

#### Web Scraped Images

Additional data was obtained through web scraping. 

Please refer to "https://keydifferences.com/difference-between-hard-skills-and-soft-skills.html" for more details related to Basis for Comparison on Hard Skills and Soft Skills

Please refer to "https://resumekit.com/blog/hard-skills-vs-soft-skills/" for more details on the soft skils vs hard skills image collected.


### Data Visualization with Tableau

To enhance the understanding of skill dynamics, impactful data visualizations were created using Tableau. The central visualization focused on the EU Access Index, shedding light on the skill ranks of different EU countries.

[EU Access Index Visualization](https://public.tableau.com/app/profile/susy.costa/viz/SkillsRankEuropeanCountries/SkillsinEurope)

## Features

1. **Image Classification**

The core functionality of the tool involves classifying user-uploaded images related to their skills and work style. This ensures a personalized and entertaining experience for each user.

2. **Skill-Based Suggestions**

Based on the image classification results, the tool provides suggestions for job skills and strengths that the user may possess. This adds a creative and humorous element to the assessment process.

3. **Social Media Integration**

Users are encouraged to share their classification results on social media, fostering a sense of engagement and networking. Please note that the shareable link feature is currently under development and will be available in future updates. 

While the shareable link feature is currently in development, stay tuned for future updates that will allow you to easily share your results.

4. **User-Friendly Interface**

The web tool features an intuitive and user-friendly interface, ensuring accessibility for users of all skill levels.

## Getting Started

**Technical Details**

The image classification is powered by a custom InceptionV3-inspired model. The architecture is designed with convolutional layers, max-pooling layers, and dense layers. The model is trained on the provided dataset for the specific image classification task.

**How to Use**

**To utilize the image classification model and interact with the Streamlit app, follow these steps:**

 1. **To obtain the Streamlit folder, you can either:**
    - Click on the "Download" button to get a ZIP file containing the project, or
    - Clone the repository to create a local copy on your machine using the following Git command:
      ```
      git clone https://github.com/your-username/your-repo.git
      ```

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

 3. **Loading the Trained Deep Learning Model:**
    - In the `app.py` file, locate the following code snippet:

      ```python
      # Load your trained Inception model outside the main app loop 
      if 'your_image_classifier_module' not in st.session_state:
          model_path = '/path/to/your/models/trained_inception_model.keras'
          st.session_state.your_image_classifier_module = load_model_function(model_path)
      ```
    
      - Update the `model_path` replacing `/path/to/your/models/` with the actual path to the folder where you keep the
      uploaded Streamlit folder and the trained Inception model.
      For example:

      ```python
      # Load your trained Inception model outside the main app loop 
      if 'your_image_classifier_module' not in st.session_state:
          model_path = '/path/to/your/models/trained_inception_model.keras'
          st.session_state.your_image_classifier_module = load_model_function(model_path)
      ```

      - Save the changes.

**Note**: Keep this file open while using the Streamlit interface.

**To explore the Streamlit visualization, follow these steps:**

  1. **Open Anaconda Command Prompt:**
   - Launch the Anaconda Command Prompt on your system.

  2. **Navigate to the Streamlit Folder:**
   - Use the `cd` command to navigate to the directory where you have downloaded the Streamlit folder.
     ```
     cd /path/to/your/streamlit/folder
     ```

  3. **Run the Streamlit App:**
   - Execute the following command to run the Streamlit app:
     ```
     streamlit run app.py
     ```

Please ensure that you have all the necessary dependencies installed in your Anaconda environment before running the app.

**Note:** If you encounter any issues with running the app, check the console output for error messages, and make sure you have activated the correct Anaconda environment.

Enjoy exploring the image classification model using "Hire Me or Not? Image Classifier Fun"!
