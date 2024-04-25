import os
from PIL import Image

WALLPAPERS_DIR = "wallpapers"
THUMBNAILS_DIR = "thumbnails"
README_FILE = "README.md"

# Ensure the thumbnails directory exists
if not os.path.exists(THUMBNAILS_DIR):
    os.mkdir(THUMBNAILS_DIR)

# Generate the thumbnails section as a string
thumbnails_section = ""
for subdir in os.listdir(WALLPAPERS_DIR):
    full_subdir_path = os.path.join(WALLPAPERS_DIR, subdir)
    
    if os.path.isdir(full_subdir_path):
        thumbnails_section += f"\n## {subdir}\n\n"
        
        thumb_subdir = os.path.join(THUMBNAILS_DIR, subdir)
        if not os.path.exists(thumb_subdir):
            os.mkdir(thumb_subdir)
        
        for image_file in os.listdir(full_subdir_path):
            valid_endings = ('.png', '.jpg', '.jpeg', '.gif')
            if image_file.endswith(valid_endings):
                full_image_path = os.path.join(full_subdir_path, image_file)
                thumb_image_path = os.path.join(thumb_subdir, image_file)
                
                with Image.open(full_image_path) as img:
                    img.thumbnail((100, 100))
                    img.save(thumb_image_path)
                
                img_str = f"[![{image_file}]({thumb_image_path})]"
                thumbnails_section += f"{img_str}({full_image_path}) "

        thumbnails_section += "\n"

# Update README content between the markers with the thumbnails section
with open(README_FILE, "r") as f:
    readme_content = f.read()

start_marker = "<!-- THUMBNAILS_START -->"
end_marker = "<!-- THUMBNAILS_END -->"
prefix = readme_content.split(start_marker)[0]
suffix = readme_content.split(end_marker)[1]

new_content = f"{prefix}{start_marker}\n{thumbnails_section}\n{end_marker}{suffix}"

with open(README_FILE, "w") as f:
    f.write(new_content)

print("Process complete.")

