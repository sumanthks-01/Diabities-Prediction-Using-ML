**Diabetes Prediction Using ML**
 
This project is a web-based application that uses machine learning to predict the risk of a person having diabetes based on a set of health-related parameters. The app provides a simple and user-friendly interface for individuals to input their data and receive an instant prediction.

**🌟 Features**
Interactive Interface: Built with Streamlit, the application offers a clean and intuitive web form for data entry.

Machine Learning Model: Utilizes a Random Forest Classifier trained on a diabetes prediction dataset to make accurate predictions.

Real-time Predictions: The model provides an immediate "Positive" or "Negative" result based on the user's input.

Simple Setup: The project is easy to set up and run locally, with minimal dependencies.

**🛠️ Installation**
To get this project running on your local machine, you'll need Python and a few libraries.

**🚀 Usage**
Once you have installed the dependencies and updated the dataset path, you can run the application with a single command.
Navigate to the project directory if you are not already there.

Run the Streamlit application:

Bash

streamlit run <your-python-file-name>.py
Open the link provided in your terminal (usually http://localhost:8501) to access the web application.

Input your data into the form fields and click the Submit button to receive a prediction.

**📊 How It Works**
The application follows a standard machine learning workflow:

Data Preprocessing: It uses OrdinalEncoder from scikit-learn to convert categorical features like gender and smoking_history into numerical values that the model can understand.

Model Training: The code splits the dataset into training and testing sets, then trains a Random Forest Classifier on the training data. This ensemble model is well-suited for classification tasks and generally provides high accuracy.

Prediction: When a user enters their data, the application uses the trained model to predict whether the person is likely to have diabetes (represented by 1) or not (0).

Result Display: Based on the model's output, it displays a clear "Negative" or "Positive" result on the web page.

**Important Note**
This tool is for educational and illustrative purposes only. It is not a substitute for professional medical advice. Always consult with a qualified healthcare professional for any health concerns or before making medical decisions.
