# 📖 User Manual

## 🌟 **1. Introduction**

Welcome to the **AI-Based Fish Disease Detection System**. This intelligent system allows fish farmers and researchers to quickly detect fish diseases using a deep learning model. By simply uploading or capturing an image of a fish, users can receive immediate disease predictions and suggested next steps making disease management faster and more accessible.

---

## 💻 **2. Installation and Setup**

To run the **FinScan Fish Disease Detection** app on your computer, follow these simple steps.

### **2.1 Get the Project Files**

First, download the project files from GitHub.

Open your terminal:

- **Windows**: Command Prompt or PowerShell
- **macOS/Linux**: Terminal

Navigate to the folder where you want to save the project.

Type:

```bash
git clone https://github.com/mayengtinloi/FinScan-Fish-Disease-Detection
````

This will create a folder named **FinScan-Fish-Disease-Detection** with all project files.

Move into the project folder:

```bash
cd FinScan-Fish-Disease-Detection
```

### **2.2 Set Up the Virtual Environment**

A virtual environment isolates project libraries to avoid conflicts.

> **📌 Requires Python 3.10 or higher.**

Check your Python version:

```bash
python --version
```

If it is not 3.10 or higher, download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### **macOS/Linux**

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

#### **Windows**

```bash
py -3.10 -m venv .venv
.\.venv\Scripts\activate
```

After activating, you should see `(.venv)` at the start of your terminal line.

Then, move into the `src` folder where all the code resources (including the model) are located:

```bash
cd src
```

### **2.3 Install Required Libraries**

Install the libraries listed in `requirements.txt`.

With your virtual environment active, type:

```bash
pip install -r requirements.txt
```

This will install:

* **streamlit** – web app interface
* **tensorflow** – AI model
* **numpy, pandas, matplotlib, scikit-learn** – data handling and analysis
* **Pillow** – image processing

---

### **2.4 Run the Application**

With everything installed, you can now start the app.

Make sure your virtual environment is still active, then type:

```bash
streamlit run FishDiseaseApplication.py
```

After a few seconds, you will see a message like:

```bash
Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501
```

Copy the local URL (e.g., `http://localhost:8501`) and paste it into your browser to open and use the application.

---

## 🧭 **3. Navigation of Prototype**

This section provides step-by-step guidance on how to use the fish disease detection prototype, including language selection, appearance settings, image submission, result interpretation, and error handling.

---

### **3.1 Language Settings**

The prototype supports multiple languages to enhance accessibility for users of different backgrounds.

To change the language:

1. Navigate to the **Language Settings** section in the application.
2. Select your preferred language from the following options:

   * English
   * Malay
   * Chinese
3. The interface will automatically update to reflect the selected language.

---

### **3.2 Appearance Settings**

Users may choose between two interface display modes based on their preference and environment.

Steps:

1. Go to the **Appearance Settings** section.
2. Select one of the following modes:

   * **Light Mode** – Best for bright surroundings.
   * **Dark Mode** – Ideal for low-light or night-time usage.
3. The selected theme will be applied throughout the application.

---

### **3.3 Fish Detection**

To detect diseases in your fish, follow these steps:

1. On the main screen, choose one of the image input options:

   * **Upload Picture** – Select an existing image of the fish from your device.
   * **Take Photo of Your Fish** – Use the camera to capture a real-time image.
2. After selecting or capturing the image, click the **Check Now** button to initiate the disease detection process.
3. The system will analyze the image using the trained AI model.

---

### **3.4 Disease Detection Result**

If a fish disease is detected, the system will display the following information:

* **Status**: Indicates whether a disease is present.
* **Disease Type**: Name of the disease identified (e.g., *Aeromoniasis*).
* **Confidence Score**: The model’s confidence level in percentage.
* **Scan Time**: The date and time the image was processed.

You will also have two action buttons:

* **Guide**: Click to view suggested treatments and handling methods for the identified disease.
* **Check Another**: Click to start a new detection with a different image.

---

### **3.5 Error Handling**

If the uploaded or captured image is not recognized as a valid fish image, the system will return the following error message:

```
Unable to detect. Try again.
```

In this case, ensure the image clearly shows a fish and try uploading or capturing it again.

