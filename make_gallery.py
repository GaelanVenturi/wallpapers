import os
from PIL import Image

WALLPAPERS_DIR = "wallpapers"
THUMBNAILS_DIR = "thumbnails"
README_FILE = "README.md"

# Ensure the thumbnails directory exists
if not os.path.exists(THUMBNAILS_DIR):
    os.mkdir(THUMBNAILS_DIR)

# Open the README file for writing
with open(README_FILE, "w") as f:
    # Iterate over each subdirectory in the wallpapers directory
    for subdir in os.listdir(WALLPAPERS_DIR):
        full_subdir_path = os.path.join(WALLPAPERS_DIR, subdir)
        
        if os.path.isdir(full_subdir_path):
            f.write(f"\n## {subdir}\n\n")  # Write header for the category
            
            # Ensure corresponding directory in thumbnails exists
            thumb_subdir = os.path.join(THUMBNAILS_DIR, subdir)
            if not os.path.exists(thumb_subdir):
                os.mkdir(thumb_subdir)
            
            # Iterate over each image in the subdirectory
            for image_file in os.listdir(full_subdir_path):
                if image_file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    full_image_path = os.path.join(full_subdir_path, image_file)
                    thumb_image_path = os.path.join(thumb_subdir, image_file)
                    
                    # Create and save thumbnail
                    with Image.open(full_image_path) as img:
                        img.thumbnail((100, 100))
                        img.save(thumb_image_path)
                    
                    # Write link to README with thumbnail
                    f.write(f"![{image_file}]({thumb_image_path}) [Full Image]({full_image_path})\n\n")

print("Process complete.")

