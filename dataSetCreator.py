import random
import os
from PIL import Image

def createDataSet(width, height, size):
    for i in range(size):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        image = Image.new('RGB', (width, height), color)
        path = os.path.join('DataSet', str(i)+'.png')
        image.save(path)
        
createDataSet(10, 10, 5000)