import streamlit as st

def show():
    # Set page title
    st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🚀 Welcome to ML Explorer</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 18px; color: #666;'>
        A powerful tool to train, analyze, and deploy machine learning models with ease.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Key Features in a grid layout
    st.markdown("""
    <style>
    .feature-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class='feature-box'>
        <h4>📊 Dataset Management</h4>
        <ul>
            <li>Load and store datasets (Titanic, Iris, Mushrooms, etc.)</li>
            <li>Persistent storage for future use</li>
            <li>Easy dataset selection & management</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature-box'>
        <h4>🔮 Predictions</h4>
        <ul>
            <li>Predict outcomes on new data</li>
            <li>Batch predictions support</li>
            <li>Downloadable results</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-box'>
        <h4>🤖 Model Training</h4>
        <ul>
            <li>Train multiple ML models</li>
            <li>Support for Logistic Regression, Random Forest, SVM, XGBoost</li>
            <li>Automatic model saving & versioning</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='feature-box'>
        <h4>📈 Visualization & Analysis</h4>
        <ul>
            <li>Performance metrics & SHAP values</li>
            <li>Evidently AI for model monitoring</li>
            <li>Data drift detection</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    ### 🚀 Getting Started
    1️⃣ **Go to 'Dataset Load'** to upload or select a dataset  
    2️⃣ **Train models** in the 'Train Models' section  
    3️⃣ **Make predictions** using the 'Predictions' page  
    4️⃣ **Visualize & analyze results** in the 'Visualization' tab  
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit</p>
        <p>For support, contact us at <a href='#'>support@mlexplorer.com</a></p>
    </div>
    """, unsafe_allow_html=True)