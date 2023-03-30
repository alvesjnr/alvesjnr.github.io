import os
from PIL import Image


HERE = os.path.dirname(os.path.abspath(__file__))
dir_path = os.path.join(HERE, "assets", "images",)

# Set the maximum size for the thumbnails
max_size = 200

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg") and "thumbnail" not in filename.lower():
        # Open the image and resize it to create a thumbnail
        with Image.open(os.path.join(dir_path, filename)) as im:
            im.thumbnail((max_size, max_size))
            # Save the thumbnail with "_thumbnail" appended to the filename
            thumbnail_filename = os.path.splitext(filename)[0] + ".thumbnail.jpg"
            im.save(os.path.join(dir_path, thumbnail_filename))