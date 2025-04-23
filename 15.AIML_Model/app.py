import streamlit as st
from pages import Home, Dataset_Load, Train_Models, Upload_Predict, Visualization

# Set page configuration
st.set_page_config(
    page_title="ML Odyssey",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Custom CSS for unique styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #2A2D3E;
        color: #F4F4F4;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #0078D7;
        color: white;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #005FA3;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: bold;
        color: #444;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://via.placeholder.com/150", use_container_width=True)  # ✅ Fixed
    st.title("🤖 ML Odyssey")
    st.markdown("---")

    # Navigation menu
    selected_page = st.radio(
        "Menu",
        ["Home", "Dataset Load", "Train Models", "Upload Predict", "Visualization"],
        index=0
    )

    st.session_state["page"] = selected_page  # ✅ Fixed

    # Quick Guide Section
    st.markdown("""
    ### ⚡ Quick Guide
    - 📊 Upload datasets for AI training
    - 🔬 Train models effortlessly
    - 🚀 Predict results with AI
    - 📈 Gain insights from data
    """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Developed with ❤️ using Streamlit</p>
        <p>Version 3.0.0</p>
    </div>
    """, unsafe_allow_html=True)

# Page rendering logic
if st.session_state["page"] == "Home":
    Home.show()
elif st.session_state["page"] == "Dataset Load":
    Dataset_Load.show()
elif st.session_state["page"] == "Train Models":
    Train_Models.show()
elif st.session_state["page"] == "Upload Predict":
    Upload_Predict.show()
elif st.session_state["page"] == "Visualization":
    Visualization.show()
