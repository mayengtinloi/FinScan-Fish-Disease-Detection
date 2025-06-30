import os
import numpy as np
import pandas as pd
from PIL import Image

# --- INPUT FOLDER ---
source_base = r'C:\Users\User\Desktop\MayDegree\sem6\machine learning\Assignment\dataset\SB-FishDisease\SB-FishDisease'

# --- OUTPUT FOLDERS ---
target_base = r'C:\Users\User\Desktop\MayDegree\sem6\machine learning\Assignment\dataset\SB-FishDisease\Extracted'
normalized_base = r'C:\Users\User\Desktop\MayDegree\sem6\machine learning\Assignment\dataset\SB-FishDisease\normalize_images'
os.makedirs(target_base, exist_ok=True)
os.makedirs(normalized_base, exist_ok=True)

# --- CORRUPTED LOG FILE ---
corrupted_log_path = os.path.join(target_base, 'corrupted_images.txt')
corrupted_images = []

# --- For intermediate CSV ---
csv_rows = []

# --- Step 1: Preprocess and save resized .jpgs ---
for folder_name in os.listdir(source_base):
    source_folder = os.path.join(source_base, folder_name)
    if not os.path.isdir(source_folder):
        continue

    target_folder = os.path.join(target_base, folder_name)
    os.makedirs(target_folder, exist_ok=True)

    count = 1
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Only handle image files
        if not file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')):
            continue

        try:
            img = Image.open(file_path).convert('RGB')
            img = img.resize((224, 224))

            new_filename = f"{folder_name} ({count}).jpg"
            save_path = os.path.join(target_folder, new_filename)
            img.save(save_path, format='JPEG')

            relative_path = os.path.relpath(save_path, target_base).replace("\\", "/")

            csv_rows.append({
                'Folder Name': folder_name,
                'Image Filename': new_filename,
                'Image Path': relative_path
            })

            count += 1

        except Exception as e:
            error_message = f"{file_path} | Reason: {e}"
            print(f" Failed to process: {error_message}")
            corrupted_images.append(error_message)

# --- Save intermediate CSV ---
csv_path = os.path.join(target_base, 'image_index.csv')
df = pd.DataFrame(csv_rows)
df.to_csv(csv_path, index=False)

if corrupted_images:
    with open(corrupted_log_path, 'w', encoding='utf-8') as f:
        for item in corrupted_images:
            f.write(item + '\n')
    print(f"\n {len(corrupted_images)} corrupted images logged to: {corrupted_log_path}")
else:
    print("\n No corrupted images found.")

print(f"\n STEP 1 DONE: {len(csv_rows)} images processed, resized, and saved to: {target_base}")
print(f" CSV saved to: {csv_path}")

# --- Step 2: Normalize pixels and one-hot encode labels ---

# Reload the CSV just to be sure
df = pd.read_csv(csv_path)

# Unique class names
classes = sorted(df['Folder Name'].unique())
class_to_index = {label: i for i, label in enumerate(classes)}
num_classes = len(classes)

rows = []
for _, row in df.iterrows():
    try:
        label = row['Folder Name']
        filename = row['Image Filename']
        image_path = os.path.join(target_base, row['Image Path'].replace('/', '\\'))

        # Load and normalize
        img = Image.open(image_path).convert('RGB')
        img_array = np.asarray(img) / 255.0  # normalize to [0, 1]

        # Save as .npy
        base_name = os.path.splitext(filename)[0]
        npy_filename = base_name + '.npy'
        npy_path = os.path.join(normalized_base, npy_filename)
        np.save(npy_path, img_array)

        # One-hot encoding
        label_index = class_to_index[label]
        one_hot = [0] * num_classes
        one_hot[label_index] = 1

        # Save row
        row_data = {
            'filename': npy_filename,
            'label': label,
            **{f'class_{i}': one_hot[i] for i in range(num_classes)}
        }
        rows.append(row_data)

    except Exception as e:
        print(f" Error processing {row['Image Path']}: {e}")

# Save final CSV
final_df = pd.DataFrame(rows)
output_csv_path = os.path.join(normalized_base, 'normalized_labels.csv')
final_df.to_csv(output_csv_path, index=False)

print(f"\n STEP 2 DONE: Normalized .npy files saved to: {normalized_base}")
print(f" One-hot encoded CSV saved to: {output_csv_path}")
