# 🌟 Streamlit ML Dashboard - Dockerized with Evidently

## 📌 Project Overview
Welcome to, this project is a **containerized Streamlit application** designed for **seamless ML model monitoring** and **interactive data visualization**. This project brings together **Jupyter notebooks, auto-generated reports, and an intuitive UI** to help track ML model performance. With **Docker**, you can deploy it effortlessly, ensuring consistency across environments.

---

## 📂 Folder & File Structure

```
📦 dockerlab7
 ├── .dockerignore            # Files to exclude from Docker builds
 ├── .gitignore               # Files ignored in version control
 ├── streamlit-app/
 │   ├── app.py               # Main Streamlit application file
 │   ├── Dockerfile           # Docker setup for the Streamlit app
 │   ├── requirements.txt     # Python dependencies
 │   ├── src/
 │   │   ├── ui.py            # UI components for the Streamlit app
 │   │   ├── utils.py         # Helper functions for app functionality
 │   ├── static/
 │   │   ├── logo.png         # Project logo
 │   │   ├── preview.png      # Screenshot of the app interface
 │   ├── projects/
 │   │   ├── bike-sharing/    # Bike-sharing analysis project
 │   │   │   ├── bicycle_demand_monitoring.ipynb  # ML notebook
 │   │   │   ├── README.md    # Description of the project
 │   │   │   ├── data/        # Data folder (ignored in Git)
 │   │   │   ├── models/      # Trained models folder (ignored in Git)
 │   │   │   ├── reports/     # Generated reports from the analysis
 │   │   ├── your-project/    # Template for adding new projects
 │   │   │   ├── README.md    # Guide to add a new ML project
 │   │   │   ├── reports/     # Placeholder for new reports
```

---

## 🚀 Getting Started

### **1️⃣ Quick Setup with Docker (Recommended)**
Ensure **Docker** is installed, then run:

```sh
docker build -t streamlit-ml-app ./streamlit-app
```
```sh
docker run -p 8501:8501 streamlit-ml-app
```
🔗 Open **http://localhost:8501/** to access the interactive dashboard.

### **2️⃣ Running Locally (Without Docker)**

#### **Step 1: Set Up a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r streamlit-app/requirements.txt
```

#### **Step 2: Launch the Streamlit App**
```sh
cd streamlit-app
streamlit run app.py
```
🔗 Visit **http://localhost:8501/** to explore the ML dashboard.

---
![Result](image.png)

## 📊 Featured ML Project - Bike Sharing Analysis
**Location:** `projects/bike-sharing/`
- 📜 **Notebook:** `bicycle_demand_monitoring.ipynb` – A deep dive into bike demand forecasting.
- 📊 **Reports:** Automated analysis on **data drift, model performance, and trends**.
- 📖 **README.md:** Full breakdown of the project methodology.

---

## 🔧 Want to Add Your Own ML Project?
1. **Create a new folder** inside `projects/`.
2. **Include a Jupyter notebook** or Python script with your analysis.
3. **Update the `README.md`** with a project description.
4. **Organize any reports, models, or data** neatly in respective folders.

---

## 🤝 Contributing & Feedback
We welcome contributions! To get started:
- 🍴 Fork the repository and clone it locally.
- 🌱 Create a new branch for your changes.
- 📢 Push your changes and open a pull request!

💡 **Suggestions?** Feel free to **raise an issue** or **start a discussion**!

🚀 **Enjoy coding & building amazing ML apps!** 🎉

