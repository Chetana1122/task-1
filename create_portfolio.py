import os

# Define folder structure
base_folder = "portfolio-website"
folders = ["images"]
files = ["index.html", "style.css", "script.js"]

# Create main folder
os.makedirs(base_folder, exist_ok=True)

# Create subfolders
for folder in folders:
    os.makedirs(os.path.join(base_folder, folder), exist_ok=True)

# Create empty files
for file in files:
    with open(os.path.join(base_folder, file), 'w') as f:
        f.write("")  # Creates empty file

# Optional: Dummy image file
image_path = os.path.join(base_folder, "images", "your_photo.jpg")
with open(image_path, 'wb') as img:
    img.write(b"")  # Empty image file (you should replace with real one)

print("✅ Portfolio folder structure created successfully!")