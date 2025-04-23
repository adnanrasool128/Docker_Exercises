# 🚀 ModelForge – Where ML models are crafted.

A powerful web application for training, analyzing, and deploying machine learning models with an intuitive user interface.

## 🌟 Features

### 📊 Dataset Management

-   Upload and store preprocessed datasets
-   Load sample datasets (Titanic, Iris, Mushrooms)
-   Persistent storage for future use
-   Easy dataset selection and management
![image](https://github.com/user-attachments/assets/a9ce0bd1-0700-4c28-bdab-80f4394307f6)


### 🎯 Model Training

-   Support for multiple ML algorithms:
    -   Logistic Regression
    -   Random Forest
    -   Support Vector Machine (SVM)
    -   XGBoost
-   Customizable model parameters
-   Automatic model saving and versioning
-   Performance metrics visualization
![image](https://github.com/user-attachments/assets/4634f3c6-cf47-4ac9-874a-f54063dc94c9)

![image](https://github.com/user-attachments/assets/261c2f20-43c9-411a-bff1-77774aa55695)

![image](https://github.com/user-attachments/assets/d576c06c-09a8-4f31-9a16-1ffc0ea5f1a6)

### 🔮 Predictions

-   Make predictions on new data
-   Download prediction results
-   Batch prediction support
-   Feature validation
![image](https://github.com/user-attachments/assets/3947ae36-d9db-4827-bfbe-000a2daa35f0)

![image](https://github.com/user-attachments/assets/6e7f6543-be1b-46da-a2d1-d833ba5038cd)


### 📈 Visualization & Analysis

-   Comprehensive model performance metrics
-   SHAP values for feature importance
-   Interactive visualizations:
    -   Feature distributions
    -   Correlation matrices
    -   ROC curves
    -   Confusion matrices
-   Statistical analysis
-   Data quality monitoring
![image](https://github.com/user-attachments/assets/12c54cfc-c7d7-4897-a38c-4d6817ac16ef)

![image](https://github.com/user-attachments/assets/bd30be44-1267-4f4a-bf61-9644900c0efe)

![image](https://github.com/user-attachments/assets/122144f1-7e7d-4fbc-82e8-603432fa7142)

![image](https://github.com/user-attachments/assets/67a1f43b-7e64-4562-9529-86ddbb7b995b)


## 🛠️ Implementation

### Tech Stack

-   **Frontend**: Streamlit
-   **ML Libraries**: scikit-learn, XGBoost
-   **Data Processing**: pandas, numpy
-   **Visualization**: plotly, matplotlib, seaborn
-   **Model Analysis**: SHAP, Evidently AI

### Project Structure

```
├── app.py                 # Main application entry point
├── utils.py               # Utility functions for ML operations
├── pages/
│   ├── Home.py            # Landing page
│   ├── Dataset_Load.py    # Dataset management
│   ├── Train_Models.py    # Model training interface
│   ├── Upload_Predict.py  # Prediction interface
│   └── Visualization.py   # Model analysis and visualization
├── models/                # Directory for saved models
└── datasets/              # Directory for datasets
```

### Key Components

#### Model Training (`utils.py`)

-   Implements model training and saving
-   Handles feature importance extraction
-   Manages model persistence

#### Dataset Management (`Dataset_Load.py`)

-   Handles file uploads
-   Manages sample datasets
-   Provides dataset preview and information

#### Model Training Interface (`Train_Models.py`)

-   Model selection and parameter tuning
-   Training progress visualization
-   Performance metrics display

#### Prediction Interface (`Upload_Predict.py`)

-   New data upload and validation
-   Prediction generation
-   Results download

#### Visualization (`Visualization.py`)

-   Model performance analysis
-   Feature importance visualization
-   Data quality monitoring

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/adnanrasool128/Docker_Exercises/tree/main/15.AIML_Model
cd AIML_Model
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## 📝 Usage Guide

1. **Load Data**

    - Upload your dataset or select a sample dataset
    - Preview and validate your data

2. **Train Model**

    - Select your target variable
    - Choose a model type
    - Adjust model parameters
    - Train and evaluate the model

3. **Make Predictions**

    - Upload new data
    - Generate predictions
    - Download results

4. **Analyze Results**
    - View model performance metrics
    - Explore feature importance
    - Analyze data quality
    - Generate visualizations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

