import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os
import random
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

os.environ['PYTHONHASHSEED'] = '90'
random.seed(90)
np.random.seed(90)
tf.random.set_seed(90)

# === Extract ML.zip ===
zip_path = "ML.zip"
extract_to = "ML"

if not os.path.exists(extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# === Load labels CSV ===
label_csv_path = os.path.join(extract_to, 'normalized_images', 'normalized_labels.csv')
df = pd.read_csv(label_csv_path)

# === Load .npy image arrays and labels ===
X, y = [], []
for _, row in df.iterrows():
    npy_path = os.path.join(extract_to, 'normalized_images', row['filename'])
    arr = np.load(npy_path)
    X.append(arr)
    y.append([row[f'class_{i}'] for i in range(len(row) - 2)])

X = np.array(X)
y = np.array(y)

# === Train-test split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Data augmentation ===
datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

# === Build MobileNetV2 model ===
def build_mobilenet_model(input_shape=(224, 224, 3), num_classes=5):
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shape)
    base_model.trainable = False

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

model = build_mobilenet_model()

# === Train model ===
history = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    epochs=12,
    validation_data=(X_test, y_test)
)

# === Evaluate ===
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = np.argmax(y_test, axis=1)

print("\nClassification Report:")
print(classification_report(y_true, y_pred))

# === Plot accuracy ===
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()
plt.grid(True)
plt.show()

# === Save model ===
#model.save('MobileNetV2.keras')
#print("Model saved as 'MobileNetV2.keras'")