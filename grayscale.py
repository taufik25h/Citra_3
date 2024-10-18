import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

path = 'C:\\SMT_5\\Pengolahan_Citra\\grayscale_image.jpg'
imgN = img.imread(path)

imgG = imgN
histogram, bin_edges = np.histogram(imgG, bins=256, range=(0, 255))

plt.figure(figsize=(10, 6))

plt.subplot(2,2,1)
plt.imshow(imgN)
plt.title("Image Grayscale ")

plt.subplot(2,2,2)
plt.plot(bin_edges[0:-1], histogram, color='black')
plt.title("Histogram Grayscale ")
plt.xlabel("Pixel Intensity ")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
