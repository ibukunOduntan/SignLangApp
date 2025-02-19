# ASL SIGN LANGUAGE LEARNING APP
## An Interactive Web Application for Learning American Sign Language Alphabet
![image](https://github.com/ibukunOduntan/SignLangApp/blob/main/asl.jpg)

### INTRODUCTION
This project aims to bridge the communication gap for individuals with hearing disabilities by providing an interactive web application to facilitate learning American Sign Language (ASL). The system leverages a **Convolutional Neural Network (CNN)** to recognize hand gestures and translate them into ASL alphabets. The web application offers a **real-time sign language recognition system**, allowing users to practice signing letters and words interactively.

The application features:
- **Real-time ASL Alphabet Recognition** using a webcam.
- **Two Learning Modes**:  
  - **Easy Mode**: Displays ASL hand signs for guidance.  
  - **Hard Mode**: Requires users to sign without reference images.
- **Text-to-ASL Converter**: Converts typed text into ASL hand signs for learning.
  
By integrating **computer vision** and **deep learning**, this project provides an engaging platform for both beginners and advanced learners to improve their ASL skills.
![image](https://github.com/user-attachments/assets/placeholder.png)

### PROBLEM STATEMENT
- Many individuals who are deaf or hard of hearing rely on **ASL**, but not everyone in society understands it.
- Existing sign language learning tools often lack **real-time interaction** and **engaging learning features**.
- A more **accessible, AI-powered** approach is needed to make ASL learning more effective.

### AIM OF THE PROJECT
- Develop an interactive **web-based ASL learning application**.
- Use **machine learning (CNN)** to recognize and classify static ASL alphabet gestures.
- Provide an engaging **user experience** with different learning modes.
- Deploy the model in real-time on a **Flask-based web application**.

### METHODOLOGY
- **STEP 1: Data Acquisition**  
  - Collected **44,654 images** of ASL alphabets using OpenCV’s **HandDetector** module.
  - Split data into **training (20772 images), validation (8903 images), and test (14979 images)** sets.  

- **STEP 2: Data Preprocessing**  
  - Applied **image resizing, grayscale conversion, and normalization**.  
  - Augmented data to improve model generalization.  

- **STEP 3: Model Training**  
  - Built a **Convolutional Neural Network (CNN)** with three convolutional layers.  
  - Used **Adam optimizer** and **categorical cross-entropy loss function**.  
  - Trained for **five epochs** to achieve high accuracy.  

- **STEP 4: Model Evaluation**  
  - Achieved **99.86% training accuracy, 99.94% validation accuracy, and 94.68% test accuracy**.
  - Used **precision, recall, F1-score, and confusion matrix** for performance analysis.  

- **STEP 5: Web Application Development**  
  - Developed a web-based interface using **Flask, HTML, CSS, and JavaScript**.  
  - Integrated **real-time gesture recognition** using webcam input.  

- **STEP 6: Model Deployment**  
  - Deployed on a **Flask server** with real-time ASL gesture detection.  

![image](https://github.com/user-attachments/assets/placeholder.png)

### TECH STACK
#### **Machine Learning & AI**
- **TensorFlow & Keras** – CNN model training and deployment  
- **OpenCV** – Hand tracking and image processing  
- **Mediapipe** – Hand landmark detection  

#### **Web Development**
- **Flask** – Backend framework  
- **HTML, CSS, JavaScript** – Frontend design and interactivity  

### RESULTS & PERFORMANCE ANALYSIS
- **Achieved 94.68% test accuracy**, making it **highly effective for real-world ASL recognition**.
- Successfully **deployed on a web interface**, making ASL learning more accessible.
- **Provides real-time feedback**, making the learning experience interactive and user-friendly.
![image](https://github.com/user-attachments/assets/placeholder.png)

### KEY INSIGHTS
- **High Accuracy**: The CNN model demonstrates strong performance in recognizing ASL gestures.
- **Real-Time Learning**: The interactive nature of the web app enhances user engagement.
- **Scalability**: The system can be extended to recognize **dynamic ASL words and phrases** in the future.

### FUTURE IMPROVEMENTS
- Extend the model to recognize **full ASL words and sentences**.
- Improve real-time **gesture tracking** using more advanced **pose estimation models**.
- Develop a **mobile version** of the application for easier accessibility.
- Integrate **speech-to-text** and **text-to-ASL animation** features.

### CONCLUSION
This project successfully developed an **AI-powered ASL learning application**, demonstrating the potential of machine learning in **assistive technology**. By providing an interactive, **real-time gesture recognition system**, the project contributes to **improving ASL accessibility and education**.
