# 📖 User Manual

## 🌟 Introduction
Welcome to the **AI-Based Fish Disease Detection System**. This intelligent system allows fish farmers and researchers to quickly detect fish diseases using a deep learning model. By simply uploading or capturing an image of a fish, users can receive immediate disease predictions and suggested next steps — making disease management faster and more accessible.

## 💻 **2. Installation and Setup**
To run the **FinScan Fish Disease Detection** app on your computer, follow these simple steps.

###  **Step 2.1: Get the Project Files**
First, download the project files from GitHub.
Open your terminal:
* **Windows**: Command Prompt or PowerShell
* **macOS/Linux**: Terminal
Navigate to the folder where you want to save the project.
Type:

```bash
git clone https://github.com/mayengtinloi/FinScan-Fish-Disease-Detection
```

This will create a folder named **FinScan-Fish-Disease-Detection** with all project files.
Move into the project folder:
```bash
cd FinScan-Fish-Disease-Detection
```
You’re now inside the project directory.


### **Step 2.2: Set Up the Virtual Environment**
A virtual environment isolates project libraries to avoid conflicts.
**📌 Requires Python 3.10 or higher.**
Check your Python version:

```bash
python --version
```

If it is not 3.10 or higher, download from:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)


#### ✅ **macOS/Linux**

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

---

#### ✅ **Windows**

```bash
py -3.10 -m venv .venv
.\.venv\Scripts\activate
```

After activating, you should see `(.venv)` at the start of your terminal line.


### 🔹 **Step 2.3: Install Required Libraries**
Install the libraries listed in `requirements.txt`.
With your virtual environment still active, type:

```bash
pip install -r requirements.txt
```

This will install:
* **streamlit** – web app interface
* **tensorflow** – AI model
* **numpy, pandas, matplotlib, scikit-learn** – data handling and analysis
* **Pillow** – image processing

### 🔹 **Step 2.4: Get the Project Files**
With everything installed, you can now start the app.
Make sure your virtual environment is still active, then type:

```bash
streamlit run FishDiseaseApplication.py
```
After a few seconds, you will see a message in your terminal that looks like this:

```bash
Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501
```
Copy the local URL (e.g., http://localhost:8501) and paste it into your browser to open and use the application.

