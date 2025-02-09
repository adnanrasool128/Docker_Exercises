🚀 Streamlit Dockerized App – Interactive Data Visualization

Welcome to Streamlit Dockerized App! 🎉 This project showcases an interactive spiral visualization using Streamlit and Altair charts, fully containerized with Docker for easy deployment. Whether you're new to Streamlit, Docker, or interactive data apps, this guide will walk you through everything you need! 🐳✨

---

📌 Project Overview
This application dynamically generates a spiral graph based on user inputs using Streamlit sliders. The app is designed to run inside a Docker container, making it highly portable and environment-independent. It includes:

✅ A Streamlit web application for interactive visualization 📊  
✅ Dockerized environment for hassle-free deployment 🐳  
✅ Mathematical computations to create a beautiful spiral pattern 🔢  

---

🏗️ Project Structure

📂 DockerLab2
│── 📜 docker-compose.yml         Standard Docker Compose configuration
│── 🛠️ docker-compose.debug.yml   Debugging-enabled Compose file
│── 📄 dockerfile                 Docker build instructions
│── 📦 requirement.txt            Required dependencies
│── 📂 src/
│   │── 🎨 stream.py              Streamlit app generating a spiral
│── 📖 README.md                  Project documentation

---

🔧 Prerequisites
Before running the app, ensure you have:

- Docker installed → [Get Docker](https://www.docker.com/get-started) 🐳  
- Python 3.x installed (if running locally)  
- Streamlit and other dependencies installed (`requirement.txt`)

---

🚀 Running the Application
 1️⃣ Running Locally (Without Docker)
If you prefer running the app without Docker, follow these steps:
```
pip install -r requirement.txt
streamlit run stream.py
```
Then, open your browser and navigate to:
```
http://localhost:8501
```

 2️⃣ Running Inside a Docker Container
To start the application inside Docker:
```
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```
Then, open:
```
http://localhost:8501
```

---

 📜 Understanding the Code
 🔹 `stream.py` – The Streamlit App
- Uses Altair charts to visualize a spiral pattern.
- Takes user input via sliders (`total_points`, `num_turns`).
- Performs mathematical calculations to generate the spiral.
- Displays an interactive chart inside a Streamlit app.

 🔹 `requirement.txt` – Dependencies
- Lists required libraries (`streamlit`, `altair`, `pandas`).
- Ensures the correct environment is set up for execution.

 🔹 `Dockerfile` – Containerizing the App
- Sets up the Python environment.
- Installs necessary dependencies (`streamlit`, `altair`, etc.).
- Copies `stream.py` into the container.
- Runs the Streamlit app.

---

 🎯 Customization & Enhancements
Want to tweak the app? Here are some ideas:
- 🎨 Change the visualization → Modify `altair_chart` in `stream.py`.
- ⚡ Optimize Dockerfile → Use multi-stage builds.
- 🛠️ Add authentication → Secure the app with Streamlit secrets.

---

 💡 Troubleshooting
❓ Port 8501 already in use? Run:
```
docker ps   Check running containers
docker stop <container_id>   Stop conflicting container
```

❓ Changes not reflecting? Rebuild the container:
```
docker build --no-cache -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

---

 🙌 Feedback & Contributions
Have suggestions or improvements? Feel free to:
✅ Open an issue 📝  
✅ Start a discussion 💬  
✅ Fork and contribute 🚀  

Let's build amazing apps together! 🐳🎨🚀

---

 🎉 Thank You!
Thank you for checking out this project! Hope you enjoy building and experimenting with Streamlit + Docker. 🚀 Happy coding! 😃

