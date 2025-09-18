import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request, jsonify
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = Flask(__name__)

# Load and preprocess data
df = pd.read_csv(r"E:\Diabities_Prediction\data\diabetes_prediction_dataset.csv")

enc = OrdinalEncoder()
df["smoking_history"] = enc.fit_transform(df[["smoking_history"]])
df["gender"] = enc.fit_transform(df[["gender"]])

x = df.drop("diabetes", axis=1)
y = df["diabetes"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = RandomForestClassifier().fit(x_train, y_train)

@app.route('/')
def index():
    # Calculate average values for placeholders
    avg_bmi = round(df['bmi'].mean(), 1)
    avg_hba1c = round(df['HbA1c_level'].mean(), 1)
    avg_glucose = round(df['blood_glucose_level'].mean(), 1)
    
    averages = {
        'bmi': avg_bmi,
        'hba1c_level': avg_hba1c,
        'blood_glucose_level': avg_glucose
    }
    
    return render_template('index.html', averages=averages)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        gender_dict = {'Female': 0.0, 'Male': 1.0, 'Other': 2.0}
        hypertension_dict = {'No': 0, 'Yes': 1}
        heart_disease_dict = {'No': 0, 'Yes': 1}
        smoking_history_dict = {'Never': 4.0, 'No Info': 0.0, 'Current': 1.0, 
                               'Former': 3.0, 'Ever': 2.0, 'Not Current': 5.0}
        
        user_data = np.array([[
            gender_dict[data['gender']],
            float(data['age']),
            hypertension_dict[data['hypertension']],
            heart_disease_dict[data['heart_disease']],
            smoking_history_dict[data['smoking_history']],
            float(data['bmi']),
            float(data['hba1c_level']),
            float(data['blood_glucose_level'])
        ]])
        
        result = model.predict(user_data)[0]
        prediction = "Negative" if result == 0 else "Positive"
        
        return jsonify({'success': True, 'prediction': prediction})
    
    except Exception as e:
        return jsonify({'success': False, 'error': 'Please fill all required fields correctly'})

if __name__ == '__main__':
    app.run(debug=True)