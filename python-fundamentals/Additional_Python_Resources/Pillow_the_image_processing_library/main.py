import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://cdn.pixabay.com/photo/2020/07/14/11/22/graphic-5403808_960_720.png")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image." + image.format
try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image.")

