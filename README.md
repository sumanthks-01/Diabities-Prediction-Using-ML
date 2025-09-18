**Diabetes Prediction Using ML**
 
This project is a web-based application that uses machine learning to predict the risk of a person having diabetes based on a set of health-related parameters. The app provides a modern, interactive interface with colorful animations for users to input their data and receive instant predictions.

**🌟 Features**
- **Modern HTML Interface**: Beautiful gradient design with smooth hover animations and interactive form elements
- **Machine Learning Model**: Utilizes a Random Forest Classifier trained on a diabetes prediction dataset for accurate predictions
- **Real-time Predictions**: Instant "Positive" or "Negative" results with color-coded feedback
- **Smart Input Guidance**: Average values displayed as placeholders to help users understand expected ranges
- **Responsive Design**: Clean two-column layout that works across different screen sizes
- **Visual Feedback**: Animated results with smooth transitions and hover effects

**🛠️ Installation**
```bash
pip install -r requirements.txt
```

**🚀 Usage**

### Local Development
1. Navigate to the project directory
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://localhost:5000`
4. Fill in the form with health parameters and click Submit to get your prediction

### Vercel Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Login to Vercel: `vercel login`
3. Deploy: `vercel --prod`
4. Your app will be live at the provided URL

**📊 How It Works**
1. **Data Preprocessing**: Uses OrdinalEncoder to convert categorical features (gender, smoking_history) into numerical values
2. **Model Training**: Random Forest Classifier trained on 70% of the dataset with 30% reserved for testing
3. **Web Interface**: Flask backend serves HTML form with JavaScript for real-time interaction
4. **Prediction**: User input is processed through the trained model via REST API
5. **Visual Results**: Color-coded results with smooth animations provide immediate feedback

**🎨 Interface Features**
- Gradient purple background with modern styling
- Hover animations on form elements
- Focus effects with glowing borders
- Animated result display with color coding
- Average value placeholders for user guidance

**⚠️ Important Note**
This tool is for educational and illustrative purposes only. It is not a substitute for professional medical advice. Always consult with a qualified healthcare professional for any health concerns or before making medical decisions.

**📁 Project Structure**
```
Diabities_Prediction/
├── app.py                 # Flask backend application
├── api/
│   └── index.py          # Vercel entry point
├── templates/
│   └── index.html        # HTML frontend with animations
├── data/
│   └── diabetes_prediction_dataset.csv
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
└── README.md             # Project documentation
```
