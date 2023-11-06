from rembg import remove 
from PIL import Image
import matplotlib.pyplot as plt

input_path = 'pic.jpg'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
plt.imshow(input)
plt.imshow(output)
