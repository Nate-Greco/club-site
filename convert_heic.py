import subprocess
import sys

# Install packages
print("Installing required packages...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "pillow-heif", "-q"])

# Convert the image
from pillow_heif import register_heif_opener
from PIL import Image

print("Converting HEIC to WebP...")
register_heif_opener()
img = Image.open(r"d:\Moved_Docs\club-site\resources\circuitBoard.HEIC")
img.save(r"d:\Moved_Docs\club-site\resources\circuitBoard.webp", "WEBP", quality=85)
print("Done! Image saved to d:\Moved_Docs\club-site\resources\circuitBoard.webp")
