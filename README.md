# 🐟 AI-Based Fish Disease Detection System

This project introduces an **AI-powered fish disease detection system** using a deep learning model, designed to be lightweight and efficient enough for potential integration into mobile applications.

## 🎯 Project Overview
Aquaculture, especially small to medium-scale fish farming, often faces major challenges in early disease detection. Delays in identifying fish diseases can lead to significant economic losses, high mortality rates, and reduced production quality.

This project aims to address these challenges by providing an easy-to-use, AI-powered fish disease detection system. By simply capturing or uploading a fish image, farmers can receive instant feedback on possible diseases and suggested management steps.

Key goals of this project include:
* Reducing dependency on manual inspection and expert-only diagnosis.
* Providing a **fast and reliable tool** to improve response time and reduce fish mortality.
* Enabling data-driven fish farming practices that can lead to higher productivity and better disease management.
* Offering a scalable solution that can potentially be deployed as a **mobile or web-based application**, making it practical even in rural or on-site environments.


# 🚀 Model Deployment

For this project, we focused on utilizing **Convolutional Neural Network (CNN) architectures** to achieve accurate and efficient fish disease classification.  
We undergo **Model Selection** with four different pre-trained models to find the most suitable one for deployment:
- **MobileNetV2**, **MobileNetV3Small**, **MobileNetV3Large**, **EfficientNetB0**
- **Input**: Fish images (captured or uploaded), resized to 224x224 pixels and normalized.
- **Output**: Classification into one of five classes:
  - Bacterial Red Disease
  - Aeromoniasis
  - Healthy
  - Parasitic Disease
  - Viral White Tail Disease
    
### ⭐ Model Chosen: MobileNetV2
We selected **MobileNetV2** as the final model for this project because it offers an excellent balance of accuracy, lightweight design, and fast performance. It is specifically optimized for devices with limited resources and provides efficient, real-time inference, making it ideal for on-site or mobile deployment.


## 🧪 Prototype
A functional prototype of this fish disease detection system has been developed as a proof of concept.  
The prototype demonstrates the complete pipeline:  
- 📷 Image capture or upload  
- 🔎 Automatic image preprocessing and normalization  
- 🤖 Disease classification using the trained MobileNetV2-based model  
- ✅ Instant prediction results and recommended actions for farmers


### 📱 Future Direction
- Convert the web-based prototype into a mobile application (APK) for easier field use
- Further enhance dataset size and diversity to improve accuracy
- Potential integration with farm management systems for tracking and analytics

### 💬 Impact

- Empowers farmers to act quickly, reducing economic losses and improving fish health
- Provides an affordable alternative to laboratory-based diagnostics
- Supports smarter, data-driven aquaculture practices



