# 📊 Telecom Customer Churn Prediction App

A machine learning-powered web application that predicts customer churn for telecommunications companies using Streamlit and scikit-learn.

## 🎯 Overview

This application helps telecom businesses identify customers who are likely to churn (cancel their service) by analyzing various customer attributes and service usage patterns. The app provides an intuitive web interface where users can input customer information and receive instant churn predictions.

## ✨ Features

- **Interactive Web Interface**: Built with Streamlit for a user-friendly experience
- **Real-time Predictions**: Instant churn predictions based on customer data
- **Comprehensive Input Fields**: Covers all relevant customer attributes including:
  - Demographics (Gender, Senior Citizen status, Partner, Dependents)
  - Service details (Phone service, Internet service, Contract type)
  - Usage patterns (Tenure, Monthly charges, Total charges)
  - Additional services (Online security, Tech support, Streaming services)
- **Machine Learning Model**: Pre-trained model using scikit-learn algorithms
- **SHAP Analysis**: Includes SHAP plots for model interpretability

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Customer-Churn-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to access the app

## 📁 Project Structure

```
Customer-Churn-app/
├── app.py                 # Main Streamlit application
├── model.pkl             # Pre-trained machine learning model
├── encoder.pkl           # Data encoding mappings
├── requirements.txt      # Python dependencies
├── Shap plot.png        # SHAP analysis visualization
└── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Training dataset
```

## 🔧 Usage

1. **Launch the App**: Run `streamlit run app.py` in your terminal
2. **Input Customer Data**: Fill in the customer information using the interactive form:
   - Select gender, senior citizen status, partner, and dependents
   - Choose service options (phone, internet, contract type)
   - Set tenure, monthly charges, and total charges
   - Configure additional services and features
3. **Get Prediction**: Click the "Predict" button to receive the churn prediction
4. **Interpret Results**: The app will display whether the customer is likely to churn or not

## 🧠 Model Details

- **Algorithm**: Machine learning model trained on telecom customer data
- **Features**: 19 customer attributes including demographics, services, and usage patterns
- **Output**: Binary classification (Churn/No Churn)
- **Training Data**: Based on the WA_Fn-UseC_-Telco-Customer-Churn dataset

## 📊 Input Features

### Demographics
- Gender (Male/Female)
- Senior Citizen (0/1)
- Partner (Yes/No)
- Dependents (Yes/No)

### Service Information
- Tenure (months)
- Phone Service (Yes/No)
- Multiple Lines (Yes/No/No phone service)
- Internet Service (DSL/Fiber optic/No)

### Additional Services
- Online Security (Yes/No/No internet service)
- Online Backup (Yes/No/No internet service)
- Device Protection (Yes/No/No internet service)
- Tech Support (Yes/No/No internet service)
- Streaming TV (Yes/No/No internet service)
- Streaming Movies (Yes/No/No internet service)

### Contract & Billing
- Contract (Month-to-month/One year/Two year)
- Paperless Billing (Yes/No)
- Payment Method (Electronic check/Mailed check/Bank transfer/Credit card)
- Monthly Charges ($)
- Total Charges ($)

## 🛠️ Dependencies

- **streamlit**: Web application framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization
- **shap**: Model interpretability

## 🔍 Model Interpretability

The application includes SHAP (SHapley Additive exPlanations) plots to help understand:
- Which features contribute most to churn predictions
- How individual feature values affect the prediction
- Model transparency and interpretability

## 📈 Use Cases

- **Customer Success Teams**: Identify at-risk customers for proactive retention efforts
- **Business Analysts**: Understand factors driving customer churn
- **Marketing Teams**: Target retention campaigns more effectively
- **Product Managers**: Identify service improvements to reduce churn

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the existing issues in the repository
2. Create a new issue with detailed information about your problem
3. Include system information and error messages

## 🔮 Future Enhancements

- [ ] Model retraining capabilities
- [ ] Batch prediction for multiple customers
- [ ] Customer segmentation analysis
- [ ] Retention strategy recommendations
- [ ] Real-time data integration
- [ ] Advanced analytics dashboard

---

**Built with ❤️ using Streamlit and Machine Learning**
