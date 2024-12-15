from dotenv import load_dotenv

load_dotenv()

import fal_client
from pathlib import Path
import zipfile
import io

def create_zip_in_memory(image_folder):
    memory_zip = io.BytesIO()
    with zipfile.ZipFile(memory_zip, 'w') as zf:
        image_folder = Path(image_folder)
        for image_file in image_folder.glob('*.jp*g'):  # Adjust the pattern if you use other image formats
            zf.write(image_file, image_file.name)
    memory_zip.seek(0)
    return memory_zip.getvalue()

# Specify the folder containing your images
image_folder = "/Users/spartan/Downloads/elonPics"

# Create zip archive in memory
zip_bytes = create_zip_in_memory(image_folder)

# Print zip contents
with zipfile.ZipFile(io.BytesIO(zip_bytes), 'r') as zf:
    print("Zip contents:", zf.namelist())

# Upload the zip file
url = fal_client.upload(zip_bytes, "application/zip")

print(f"Zip archive uploaded. URL: {url}")

# Use the URL in your request
handler = fal_client.submit(
    "fal-ai/flux-lora-fast-training",
    arguments={
        "images_data_url": url,
    },
)

result = handler.get()
print(result)